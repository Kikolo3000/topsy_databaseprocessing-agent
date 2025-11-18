import json
import shutil
import os
from pathlib import Path
from typing import Dict, List

def fragment_transcript(transcript_path: str, output_path: str = None) -> List[Dict]:
    """
    Fragment a clinical interview transcript into individual patient interventions with context.

    Args:
        transcript_path: Path to the transcript file
        output_path: Optional path to save the JSON output

    Returns:
        List of dictionaries containing fragmented interventions
    """
    fragments = []

    transcript_path = Path(transcript_path)

    # Read transcript
    with open(transcript_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Use parent directory name (e.g., subject_session) for fragment IDs
    base_name = transcript_path.parent.name or transcript_path.stem

    # Parse all interventions (both I: and S:)
    interventions = []
    current_speaker = None
    current_text = []
    current_line_start = None

    for line_num, line in enumerate(lines, start=1):
        line = line.rstrip('\n')

        # Skip header and section markers
        if line.startswith('Transcribed by:') or line.startswith('@'):
            continue

        # Check for speaker change
        if line.startswith('I:') or line.startswith('S:'):
            # Save previous intervention if exists
            if current_speaker is not None and current_text:
                interventions.append({
                    'line_number': current_line_start,
                    'speaker': current_speaker,
                    'text': ' '.join(current_text).strip()
                })

            # Start new intervention
            current_speaker = line[0]  # 'I' or 'S'
            current_line_start = line_num
            current_text = [line[2:].strip()]  # Remove 'X:' prefix

        elif current_speaker is not None and line.strip():
            # Continuation of current intervention (multi-line)
            current_text.append(line.strip())

    # Don't forget the last intervention
    if current_speaker is not None and current_text:
        interventions.append({
            'line_number': current_line_start,
            'speaker': current_speaker,
            'text': ' '.join(current_text).strip()
        })

    # Extract patient (S:) interventions with context
    intervention_counter = 1

    for i, intervention in enumerate(interventions):
        if intervention['speaker'] == 'S':
            # Build context: up to 5 prior interventions
            # (2 conversational turns = I, S, I, S, plus final I before current S)
            context_parts = []
            context_start_idx = max(0, i - 5)

            for j in range(context_start_idx, i):
                ctx = interventions[j]
                context_parts.append(f"{ctx['speaker']}: {ctx['text']}")

            fragment = {
                'id': f"{base_name}_{intervention_counter:04d}",
                'line_number': intervention['line_number'],
                'close_context': '\n'.join(context_parts) if context_parts else "",
                'study_excerpt': intervention['text']
            }

            fragments.append(fragment)
            intervention_counter += 1

    # Save to file if requested
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            if output_path.suffix == '.jsonl':
                for frag in fragments:
                    f.write(json.dumps(frag, ensure_ascii=False) + '\n')
            else:
                json.dump(fragments, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(fragments)} fragments to {output_path}")

    return fragments

def process_all_resources():
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    resources_dir = project_root / "resources"
    results_dir = project_root / "results"

    if not resources_dir.exists():
        print(f"Resources directory not found: {resources_dir}")
        return

    print(f"Scanning {resources_dir} for .cha files...")

    count = 0
    for cha_file in resources_dir.rglob('*.cha'):
        # Determine the directory name for the result (the transcript name)
        transcript_name = cha_file.stem

        # Create the result directory
        result_subdir = results_dir / transcript_name
        result_subdir.mkdir(parents=True, exist_ok=True)

        # 1. Run fragment_transcript and save as input.jsonl
        output_jsonl = result_subdir / "input.jsonl"
        try:
            fragment_transcript(str(cha_file), str(output_jsonl))
        except Exception as e:
            print(f"Error processing {cha_file}: {e}")
            continue

        # 2. Copy the original transcript to transcription.md
        output_md = result_subdir / "transcription.md"
        try:
            shutil.copy2(cha_file, output_md)
            print(f"Copied transcript to {output_md}")
        except Exception as e:
            print(f"Error copying transcript {cha_file}: {e}")
            continue

        count += 1

    print(f"Processed {count} files.")

if __name__ == "__main__":
    process_all_resources()
