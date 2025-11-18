import os
import sys
from pathlib import Path

# Ensure we can import clean_cha from the same directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from clean_cha import clean_cha

def process_all(input_root, output_root):
    input_root = Path(input_root)
    output_root = Path(output_root)

    if not input_root.exists():
        print(f"Error: Input directory '{input_root}' does not exist.")
        return

    count = 0
    for cha_file in input_root.rglob('*.cha'):
        # Calculate relative path to maintain structure
        rel_path = cha_file.relative_to(input_root)
        dest_path = output_root / rel_path

        # Create destination directory if it doesn't exist
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        print(f"Processing {cha_file.name}...")
        try:
            clean_cha(str(cha_file), str(dest_path))
            count += 1
        except Exception as e:
            print(f"Failed to process {cha_file}: {e}")

    print(f"Finished processing {count} files.")

if __name__ == "__main__":
    # Determine paths relative to the script location
    script_dir = Path(__file__).parent
    project_root = script_dir.parent

    input_dir = project_root / "resources_originals"
    output_dir = project_root / "resources"

    print(f"Input: {input_dir}")
    print(f"Output: {output_dir}")

    process_all(input_dir, output_dir)
