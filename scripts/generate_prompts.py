from __future__ import annotations

import re
from pathlib import Path

PLACEHOLDER = "{put_here_the_name_of_the_transcript}"
TRANSCRIPT_ASSIGNMENT_PATTERN = re.compile(r"(TRANSCRIPT_NAME=)([^\s`]+)")

def get_repo_root() -> Path:
    """Return repository root inferred from this script's location."""
    return Path(__file__).resolve().parents[1]

def list_result_subdirs(results_dir: Path) -> list[str]:
    """Return sorted list of subdirectory names inside the results directory."""
    if not results_dir.exists():
        raise FileNotFoundError(f"Results directory not found: {results_dir}")

    subdirs = [p.name for p in results_dir.iterdir() if p.is_dir()]
    if not subdirs:
        raise RuntimeError(f"No subdirectories found in results directory: {results_dir}")
    return sorted(subdirs)

def generate_prompt_content(template: str, transcript_name: str) -> str:
    # First try simple placeholder replacement
    content = template
    if PLACEHOLDER in content:
        content = content.replace(PLACEHOLDER, transcript_name)

    # Also check for the regex pattern just in case the placeholder isn't used but the pattern is
    # or if there are multiple places needing update.
    # However, the user's request specifically mentions the placeholder.
    # The provided reference code had an 'if/else' structure that might miss one if both exist.
    # Let's stick to the reference logic but ensure we handle the placeholder primarily as requested.

    if PLACEHOLDER not in template:
        # Fallback to regex if placeholder is missing
        match = TRANSCRIPT_ASSIGNMENT_PATTERN.search(template)
        if match:
            prefix, _ = match.groups()
            return (
                f"{template[:match.start()]}{prefix}{transcript_name}{template[match.end():]}"
            )
        raise ValueError(
            "Neither placeholder '{put_here_the_name_of_the_transcript}' nor a TRANSCRIPT_NAME assignment was found in MASTER_PROMPT.md"
        )

    return content

def write_prompt_file(prompts_dir: Path, transcript_name: str, content: str) -> Path:
    prompts_dir.mkdir(parents=True, exist_ok=True)
    output_path = prompts_dir / f"{transcript_name}_prompt.md"
    output_path.write_text(content, encoding="utf-8")
    return output_path

def main() -> None:
    repo_root = get_repo_root()
    master_prompt_path = repo_root / "MASTER_PROMPT.md"
    results_dir = repo_root / "results"
    prompts_dir = repo_root / "prompts_sonnet"

    if not master_prompt_path.exists():
        raise FileNotFoundError(f"MASTER_PROMPT.md not found at {master_prompt_path}")

    template = master_prompt_path.read_text(encoding="utf-8")
    transcript_names = list_result_subdirs(results_dir)

    created_files: list[Path] = []
    for transcript_name in transcript_names:
        content = generate_prompt_content(template, transcript_name)
        output_path = write_prompt_file(prompts_dir, transcript_name, content)
        created_files.append(output_path)

    print(
        f"Generated {len(created_files)} prompt files in {prompts_dir} from template {master_prompt_path}."
    )

def entry_point() -> None:
    try:
        main()
    except Exception as exc:
        raise SystemExit(f"Error: {exc}") from exc

if __name__ == "__main__":
    entry_point()
