import re
import sys

def clean_cha(input_path, output_path):
    """
    Cleans a .cha transcript, keeping:
      - metadata lines starting with '@'
      - speaker lines (*INV:, *PAR:, etc.)
    Additional operations:
      - merges consecutive utterances from the same speaker
      - normalizes speakers: INV -> I, PAR -> S
      - removes CHAT codes: [ ], { }, < >, &=..., and timestamps ...
    """

    # Regular patterns
    # Added \*\s* to speaker_line to match lines starting with *
    speaker_line = re.compile(r'^\*([A-Za-z0-9]+):\s*(.*)$')

    # Added \x15[^\x15]*\x15 to remove timestamps like 1255_6535
    # Changed &=[^\s]+ to &[^\s]+ to remove all &-fillers, &+fragments, &*codes
    bracket_codes = re.compile(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>|&[^\s]+|\x15[^\x15]*\x15')

    # Read input
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    metadata = []
    utterances = []   # (speaker, text)

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Metadata lines
        if stripped.startswith('@'):
            metadata.append(stripped)
            continue

        # Speaker lines
        m = speaker_line.match(stripped)
        if m:
            spk, text = m.groups()

            # Normalize speaker labels
            if spk == "INV":
                spk = "I"
            elif spk == "PAR":
                spk = "S"
            else:
                # Other speakers pass through unchanged
                spk = spk

            # Remove codes
            text = bracket_codes.sub('', text)

            # Remove other common CHAT symbols if needed (like +//.)
            text = text.replace('+//.', '').replace('+/.', '').replace('+"/.', '')

            # Remove xxx (unintelligible)
            text = re.sub(r'\bxxx\b', '', text)

            text = re.sub(r'\s+', ' ', text).strip()

            # Fix punctuation spacing: remove space before . , ? !
            text = re.sub(r'\s+([.,?!])', r'\1', text)

            utterances.append((spk, text))

    # Merge consecutive utterances from the same speaker
    merged = []
    prev_spk = None
    buffer = []

    for spk, text in utterances:
        if spk == prev_spk:
            # Continue same speaker
            buffer.append(text)
        else:
            # New speaker -> flush previous
            if prev_spk is not None:
                merged.append((prev_spk, " ".join(buffer)))
            prev_spk = spk
            buffer = [text]

    # Flush last speaker block
    if prev_spk is not None:
        merged.append((prev_spk, " ".join(buffer)))

    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in metadata:
            f.write(line + "\n")
        for spk, text in merged:
            # Capitalize first letter
            if text and text[0].islower():
                text = text[0].upper() + text[1:]

            # Capitalize after sentence terminators (. ? !)
            def cap_match(match):
                return match.group(1) + match.group(2).upper()

            text = re.sub(r'([.?!]\s+)([a-z])', cap_match, text)

            f.write(f"{spk}: {text}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_cha.py input.cha output.cha")
        sys.exit(1)

    clean_cha(sys.argv[1], sys.argv[2])
