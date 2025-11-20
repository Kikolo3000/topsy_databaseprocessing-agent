# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**TOPSY DATABASE**: AI-powered systematic analysis of Formal Thought Disorder (FTD) in clinical interview transcripts using the TALD (Thought and Language Disorder) scale. This system performs automated linguistic analysis to identify 16 distinct FTD domains across clinical interview data.

## Core Architecture

### Data Processing Pipeline

The system follows a three-stage pipeline:

1. **Preprocessing** (`scripts/clean_cha.py`): Cleans raw CHAT format transcripts
   - Normalizes speaker labels: `INV` → `I` (interviewer), `PAR` → `S` (subject/patient)
   - Removes CHAT codes: brackets, timestamps, filler markers
   - Merges consecutive utterances from same speaker
   - Capitalizes sentences properly

2. **Fragmentation** (`scripts/fragment_cha.py`): Breaks transcripts into analyzable units
   - Extracts patient utterances (S: speaker only)
   - Provides 5-turn conversational context window ("close_context")
   - Generates unique IDs: `{transcript_name}_{sequence:04d}`
   - Outputs to `results/{transcript_name}/input.jsonl`

3. **Analysis** (AI-driven via `MASTER_PROMPT.md`): Two-stage FTD evaluation
   - **Stage 1 (Screening)**: Rapid triage to flag potential FTDs
   - **Stage 2 (Detailed Analysis)**: Granular evaluation using domain-specific skills
   - Outputs structured JSONL with severity scores, rationales, and diagnostic metadata

### Directory Structure

```
resources_originals/     # Raw .cha files (CHAT format)
resources/               # Cleaned .cha files (normalized)
results/{transcript}/    # Per-transcript analysis workspace
  ├── transcription.md   # Full cleaned transcript
  ├── input.jsonl        # Fragmented patient interventions
  └── output_sonnet45.jsonl  # AI analysis results
skills/{FTD_CODE}/       # Domain-specific diagnostic criteria (16 FTD types)
prompts_sonnet/          # Generated per-transcript prompts
```

### FTD Domain Skills

The `skills/` directory contains 16 subdirectories (one per TALD domain), each with a `SKILL.md` file defining:
- Diagnostic criteria with clinical definitions
- Evaluation scratchpad questions (sp1, sp2, sp3...)
- Exclusion checklist items (ec1, ec2, ec3...)
- Severity scoring rubric (0-4 scale)
- Examples distinguishing presence/absence

**Domain codes**: CIR, CLA, CON, DER, DOT, ECH, MAN, NEO, PER, POC, POS, POT, RES, SEM, TAN, VER

**Special skill**: `format_validation/` - validates output.jsonl structure and completeness

## Key Workflows

### Setup New Transcript Analysis

```bash
# 1. Clean raw CHAT transcripts
python scripts/process_all.py
# Reads from: resources_originals/
# Writes to: resources/

# 2. Fragment transcripts into analysis units
python scripts/fragment_cha.py
# Reads from: resources/*.cha
# Creates: results/{transcript_name}/input.jsonl
#          results/{transcript_name}/transcription.md

# 3. Generate AI prompts for each transcript
python scripts/generate_prompts.py
# Reads: MASTER_PROMPT.md, results/*/ subdirectories
# Creates: prompts_sonnet/{transcript_name}_prompt.md
```

### Run FTD Analysis

Analysis is AI-driven following `MASTER_PROMPT.md` instructions:

1. Read full transcript: `results/{transcript_name}/transcription.md`
2. Process each line from `input.jsonl` sequentially
3. For each patient intervention:
   - **Stage 1**: Screen using one-liner definitions → flag potential FTDs
   - **Stage 2**: Deploy independent evaluations for flagged domains using `skills/{FTD_CODE}/SKILL.md`
   - Synthesize results into structured output record
4. Append to `output_sonnet45.jsonl` (one JSON object per line)
5. Validate output using `skills/format_validation/SKILL.md`

## Analysis Protocol: Critical Rules

### Context Hierarchy

Three levels available for evaluation:
- **Study excerpt**: The specific patient utterance being scored
- **Close context**: 5 prior conversational turns (from input.jsonl)
- **Full transcript**: Complete interview (transcription.md)

**When to escalate to full transcript**:
- TAN (Tangentiality), PER (Perseveration), RES (Restricted Thinking), DER (Derailment)
- Any case where close context doesn't clarify whether behavior is pathological

### Two-Stage Evaluation (Critical)

**Stage 1 never concludes FTD present** - only flags for Stage 2 confirmation. Outputs:
```json
"screening": {
  "decision": "needs_analysis" | "everything_looks_good",
  "flagged_ftds": ["POC", "TAN"],
  "screening_rationale": "Brief explanation"
}
```

**Stage 2 must complete all evaluations before synthesis**:
- Deploy independent evaluation for each flagged domain
- Each uses its specific `skills/{FTD_CODE}/SKILL.md`
- Wait until all 16 domains scored before writing rationale object

### Output Format Requirements

Every output record must include:
- All 16 domain codes with severity scores (0-4)
- `screening` object
- `rationale` object (entries for scored domains + flagged-but-absent domains)
- `scratchpad` object (only for flagged domains)
- `exclusion_checklist` object (only for flagged domains)
- `analyzed_at` timestamp (ISO 8601)

Each rationale entry: 2-4 sentence paragraph with:
- Specific quotes/patterns from study excerpt
- Justification for exact severity score
- Clinically precise language for provider review

## Development Commands

### Python Environment

```bash
# Install dependencies (currently minimal)
pip install -r requirements.txt

# Run preprocessing pipeline
python scripts/process_all.py          # Clean all raw transcripts
python scripts/fragment_cha.py         # Fragment all transcripts
python scripts/generate_prompts.py     # Generate AI prompts
```

### File Validation

The `skills/format_validation/SKILL.md` provides validation criteria. Key checks:
- All input IDs have output records
- No duplicate IDs
- Severity scores in [0-4]
- All 16 domains present per record
- Proper JSONL format (one JSON per line, no internal newlines)
- Valid ISO 8601 timestamps
- Rationale completeness (scored + flagged domains)

## Important Implementation Notes

### MASTER_PROMPT.md Template System

The `MASTER_PROMPT.md` uses a placeholder pattern:
```
TRANSCRIPT_NAME={put_here_the_name_of_the_transcript}
```

`generate_prompts.py` replaces this with actual transcript names from `results/*/` subdirectories.

### Speaker Normalization

Throughout the system:
- `I:` = Interviewer (originally `*INV:` in CHAT format)
- `S:` = Subject/Patient (originally `*PAR:` in CHAT format)

### Fragment ID Format

Pattern: `{transcript_dir_name}_{sequence:04d}`
- Example: `TOPSY-0_0001`, `001_0042`
- Sequence increments for each patient intervention in chronological order

### Subagent Independence Principle

Stage 2 evaluations should be conceptually independent:
- Each FTD domain evaluated in isolation
- No cross-contamination between domain assessments
- Each loads only its specific skill file
- Main agent synthesizes results after all domains evaluated
