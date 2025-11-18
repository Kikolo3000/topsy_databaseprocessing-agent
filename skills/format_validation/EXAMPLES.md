# Format Validation Examples

## Example 1: Basic Validation

```bash
# Validate output file only
python validate.py results/40010_fu1/output_sonnet45.jsonl
```

**Output:**
```
======================================================================
VALIDATION REPORT: results/40010_fu1/output_sonnet45.jsonl
======================================================================

✓ VALIDATION PASSED
  All checks completed successfully.

======================================================================
```

## Example 2: Validation with Input Completeness Check

```bash
# Check that all input interventions were processed
python validate.py results/40010_fu1/output_sonnet45.jsonl results/40010_fu1/input.jsonl
```

**Output if intervention missing:**
```
======================================================================
VALIDATION REPORT: results/40010_fu1/output_sonnet45.jsonl
======================================================================

✗ VALIDATION FAILED
  Found 1 error(s):

  1. Missing output for input IDs: ['40010_fu1_tran_0042']

======================================================================
```

## Example 3: Programmatic Usage

```python
from validate import validate_output_file, print_validation_report

# Run validation
is_valid, errors = validate_output_file(
    "results/40010_fu1/output_sonnet45.jsonl",
    "results/40010_fu1/input.jsonl"
)

# Print formatted report
print_validation_report(is_valid, errors, "results/40010_fu1/output_sonnet45.jsonl")

# Handle errors programmatically
if not is_valid:
    print("\nDetailed errors:")
    for error in errors:
        print(f"  - {error}")

    # Take corrective action
    # ...
else:
    print("Ready to proceed with analysis!")
```

## Example 4: Common Error Cases

### Missing Domain Score

**Error Message:**
```
Line 5: Missing TALD domains: ['TAN', 'VER']
```

**Fix:** Ensure all 16 domain codes are present:
```json
{
  "id": "40010_fu1_tran_0005",
  "CIR": 0, "CLA": 0, "CON": 0, "DER": 0,
  "DOT": 0, "ECH": 0, "MAN": 0, "NEO": 0,
  "PER": 0, "POC": 2, "POS": 0, "POT": 0,
  "RES": 0, "SEM": 0, "TAN": 0, "VER": 0,
  ...
}
```

### Invalid Score Range

**Error Message:**
```
Line 12: POC score must be 0-4, got 5
```

**Fix:** Use valid severity scores (0-4):
```json
{
  "POC": 4,  // Changed from 5 to 4 (maximum severity)
  ...
}
```

### Missing Rationale for Scored Domain

**Error Message:**
```
Line 8: Missing rationale for domain 'POC' (scored or flagged)
```

**Fix:** Add rationale entry for scored domain:
```json
{
  "POC": 2,
  "rationale": {
    "POC": "The patient's response demonstrates poverty of content with multiple filler words ('um', 'like', 'you know') that reduce informational density. While adequate in length, the response conveys minimal substantive information about the topic. This mild-to-moderate presentation (score 2) reflects vagueness occurring multiple times without rendering communication completely empty."
  },
  ...
}
```

### Inconsistent Screening Decision

**Error Message:**
```
Line 3: Decision 'everything_looks_good' but flagged_ftds is not empty
```

**Fix:** Make decision consistent with flagged_ftds:
```json
{
  "screening": {
    "decision": "everything_looks_good",
    "flagged_ftds": [],  // Must be empty for everything_looks_good
    "screening_rationale": "No FTD features detected in this intervention."
  },
  ...
}
```

### Scratchpad for Non-Flagged Domain

**Error Message:**
```
Line 15: scratchpad has entries for non-flagged domains: ['DER']
```

**Fix:** Only include scratchpad entries for flagged domains:
```json
{
  "screening": {
    "decision": "needs_analysis",
    "flagged_ftds": ["POC", "TAN"],  // Only these two were flagged
    ...
  },
  "scratchpad": {
    "POC": { ... },  // OK - flagged
    "TAN": { ... }   // OK - flagged
    // "DER": { ... } <- REMOVE - not flagged
  },
  ...
}
```

### Brief Rationale Warning

**Error Message:**
```
Line 20: Rationale for 'POC' too brief (<10 words)
```

**Fix:** Expand rationale to 2-4 sentences with detailed explanation:

**Before (too brief):**
```json
{
  "rationale": {
    "POC": "Vague speech with fillers."
  }
}
```

**After (detailed):**
```json
{
  "rationale": {
    "POC": "The patient's response demonstrates poverty of content of speech at a mild-to-moderate level (score 2). While the utterance is adequate in length, the informational density is significantly reduced due to excessive use of filler words ('um', 'well', 'like', 'you know', 'I guess') which constitute approximately 50% of the speech content. The patient names only two subjects ('science and math') without elaboration or meaningful detail. This score of 2 reflects that vagueness occurs several times but does not render communication completely empty."
  }
}
```

## Example 5: Integration in Analysis Script

```python
#!/usr/bin/env python3
"""FTD Analysis with Validation"""

from validate import validate_output_file, print_validation_report

def analyze_transcript(transcript_name):
    """Analyze a transcript and validate output."""

    # Paths
    input_file = f"results/{transcript_name}/input.jsonl"
    output_file = f"results/{transcript_name}/output_sonnet45.jsonl"

    # Step 1: Run FTD analysis
    print(f"Analyzing {transcript_name}...")
    # ... your analysis code here ...

    # Step 2: Validate output
    print(f"\nValidating output...")
    is_valid, errors = validate_output_file(output_file, input_file)
    print_validation_report(is_valid, errors, output_file)

    # Step 3: Handle results
    if is_valid:
        print(f"✓ {transcript_name} analysis complete and validated!")
        return True
    else:
        print(f"✗ {transcript_name} validation failed. Please review errors.")
        return False

# Run for transcript
if __name__ == "__main__":
    analyze_transcript("40010_fu1")
```

## Example 6: Batch Validation

```python
from pathlib import Path
from validate import validate_output_file

def validate_all_transcripts(results_dir="results"):
    """Validate all transcripts in results directory."""

    results_path = Path(results_dir)
    all_valid = True

    for transcript_dir in results_path.iterdir():
        if not transcript_dir.is_dir():
            continue

        output_file = transcript_dir / "output.jsonl"
        input_file = transcript_dir / "input.jsonl"

        if not output_file.exists():
            print(f"⚠ {transcript_dir.name}: No output file found")
            continue

        is_valid, errors = validate_output_file(
            str(output_file),
            str(input_file) if input_file.exists() else None
        )

        if is_valid:
            print(f"✓ {transcript_dir.name}: Valid")
        else:
            print(f"✗ {transcript_dir.name}: {len(errors)} error(s)")
            all_valid = False

    return all_valid

# Validate all
if __name__ == "__main__":
    all_valid = validate_all_transcripts()
    print(f"\n{'All transcripts valid!' if all_valid else 'Some transcripts have errors.'}")
```
