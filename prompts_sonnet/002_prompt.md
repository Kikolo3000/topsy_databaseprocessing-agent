# MASTER PROMPT: FTD Analysis Using TALD Scale

## Your Task

You are analyzing a clinical interview transcript to identify formal thought disorder (FTD) in every patient intervention. You will systematically evaluate each patient utterance using the TALD (Thought and Language Disorder) scale, which includes 16 distinct FTD domains.

**TRANSCRIPT_NAME**: TRANSCRIPT_NAME=002
**Transcript to analyze**: `results/{TRANSCRIPT_NAME}/transcription.md`
**Input file**: `results/{TRANSCRIPT_NAME}/input.jsonl` (fragmented patient interventions)
**Output file**: `results/{TRANSCRIPT_NAME}/output_sonnet45.jsonl` (your analysis results)

## Critical First Steps

**BEFORE analyzing any intervention:**
1. Read the ENTIRE transcript file: `results/{TRANSCRIPT_NAME}/transcription.md`
2. Keep the full transcript available for reference throughout the session
3. Then begin processing interventions from `input.jsonl` sequentially

## TALD Scale: 16 Domains with One-Liner Definitions

You will evaluate each patient intervention for these 16 FTD domains. You are equipped with an skill with a granular evaluation process for each of them, but the following should serve as an overview specially for the screening stage.

1. **Circumstantiality (CIR)**: Thinking is circuitous; minor matters cannot be separated from essential matters. The main point gets lost in the description of details, without losing the intentional goal completely (long-winded speech). *Context: Close context usually sufficient to see if details obscure the main point.*

2. **Clanging (CLA)**: A pattern of speech in which sounds, rather than meaningful relationships, appear to govern word choice, so that the intelligibility of the speech is impaired and redundant words are introduced. *Context: Usually evident from study excerpt alone.*

3. **Concretism (CON)**: Difficulty in the comprehension of abstract (figurative) sentences or phrases (e.g. proverbs, metaphors, jokes). The patient adheres to the concrete meaning of the words/utterances. *Context: Close context needed to see if figurative language was present in the exchange.*

4. **Derailment (DER)**: A pattern of spontaneous speech in which ideas slip "off the track" onto other thoughts which are clearly but obliquely related. Things may be said in juxtaposition which lack a meaningful relationship, or the patient may shift idiosyncratically from one frame of reference to another. *Context: May need full transcript to identify the original "track" and derailment pattern.*

5. **Dissociation of Thinking (DOT)**: The content of a phrase, sentence or thought has no reference to what has been said before. Words, sentences and thoughts have no relation to each other. In contrast to Derailment where associative bridges are still recognizable, Dissociation refers to the state where coherence between or within sentences is absent. *Context: Close context usually sufficient to assess lack of relation to prior speech.*

6. **Echolalia (ECH)**: Senseless repetitions of words and sentences with no regard to their meanings and semantic functions. The patient echoes the words or sentences of the interviewer. *Context: Close context essential to see interviewer's words being echoed.*

7. **Manneristic Speech (MAN)**: For the observer, speech (word selection, sentence structure, articulation or prosody) seems affected and ornate, eccentric, unnatural, pompous, overblown, fancy, stylised or flowery. *Context: Usually evident from study excerpt alone.*

8. **Neologisms (NEO)**: New word formations which do not correspond to lexical conventions. Most Neologisms are not directly intelligible. In extreme cases a new artificial language can be formed or used by the patient. *Context: Usually evident from study excerpt alone.*

9. **Perseveration (PER)**: Adherence to previously mentioned ideas and topics that no longer fit the current context. *Context: May need full transcript to see if themes recur inappropriately across the interview.*

10. **Poverty of Content of Speech (POC)**: Speech that is adequate in amount but conveys little information. Content is vague, overly abstract or overly concrete, repetitive and stereotyped. *Context: Usually evident from study excerpt and close context alone.*

11. **Poverty of Speech (POS)**: Restriction in the amount of spontaneous speech. Replies are brief, concrete, and unelaborated. *Context: Usually evident from study excerpt alone.*

12. **Poverty of Thought (POT)**: The patient has the sense that his thinking is unimaginative and restricted to just a few themes. This may or may not be accompanied by unpleasant feelings. *Context: Requires patient's subjective report; close context usually sufficient.*

13. **Restricted Thinking (RES)**: The patient repeatedly returns to or persists in discussing a limited set of topics, making conversation about other subjects difficult. *Context: May need full transcript to identify pattern of returning to limited topics.*

14. **Semantic Paraphasia (SEM)**: Substitution of an inappropriate word (the word is semantically related to the appropriate word). The speaker may or may not recognize the error and attempt to correct it. *Context: Usually evident from study excerpt alone.*

15. **Tangentiality (TAN)**: Ideas do not follow a straight path. Within longer speech passages, content slowly drifts away from where it originally started. The patient does not return to the initial topic. *Context: Often requires full transcript to trace topic drift from original starting point.*

16. **Verbigeration (VER)**: Unnecessary repetition of a single word. *Context: Usually evident from study excerpt alone.*

**Severity Scale for all domains**:
- 0 = Not present
- 1 = Doubtful (not definitely pathological)
- 2 = Mild
- 3 = Moderate
- 4 = Severe

## Three-Level Context Strategy

For each intervention, you have three levels of context available:

1. **Study Excerpt**: The specific patient utterance being evaluated (always provided in input.jsonl)
2. **Close Context**: The conversational turns immediately preceding the excerpt (provided in input.jsonl as "close_context")
3. **Full Transcript**: The complete interview you read at the start

**When to use each level:**
- **Study excerpt + close context**: Primary reference for most evaluations
- **Full transcript**: Consult when:
  - Assessing patterns over longer conversation arcs (tangentiality, perseveration)
  - Determining if topic drift is tangential vs. appropriate conversation flow
  - Understanding whether recurring themes are perseverative or contextually appropriate
  - Resolving ambiguity that close context cannot clarify

**Domain-specific guidance:**
- POC, POS, ECH, VER, MAN, CLA, NEO, SEM: Usually evident from excerpt + close context
- TAN, DER, PER, RES: Often require full transcript review
- CIR, DOT, CON: Close context typically sufficient
- **When in doubt, consult the full transcript**

## Two-Stage Analysis Process

### Stage 1: Initial Screening (Rapid Triage)

**For each intervention in input.jsonl:**

1. Read the study excerpt and close context
2. Apply the one-liner definitions above to identify potential FTDs
3. Make a binary decision:
   - **"everything_looks_good"**: No FTDs detected → Score all 16 domains as 0, write brief screening rationale, SKIP Stage 2, write output
   - **"needs_analysis"**: Possible FTDs detected → Flag specific domain codes for Stage 2

**CRITICAL RULE**: You NEVER conclude an FTD is present in Stage 1. You only flag potential FTDs for detailed confirmation in Stage 2. If you're uncertain whether something is an FTD, flag it for Stage 2 rather than dismissing it.

**Stage 1 Output** (record this for the final output):
```json
"screening": {
  "decision": "needs_analysis",  // or "everything_looks_good"
  "flagged_ftds": ["POC", "TAN"],  // empty array if everything_looks_good
  "screening_rationale": "Possible poverty of content due to vague language; potential tangential drift from question topic"
}
```

### Stage 2: Granular Analysis with Subagents (Only if needs_analysis)

**If Stage 1 flagged any FTDs, deploy independent subagents for detailed evaluation:**

**For each flagged FTD domain:**

1. **Deploy a subagent** with isolated context:
   - Provide: study excerpt, close context, access to full transcript, the specific FTD code to evaluate
   - Subagent use skills: `skills/{FTD_CODE}/SKILL.md` (e.g., `skills/POC/SKILL.md`)

2. **Subagent evaluation process**:
   - Read the complete skill file for detailed diagnostic criteria
   - Work through the evaluation scratchpad questions (sp1, sp2, sp3, etc.)
   - Apply the exclusion checklist criteria (ec1, ec2, ec3, etc.)
   - Determine severity score (0-4) based on detailed criteria
   - Write domain-specific rationale explaining the score

3. **Subagent returns**:
   ```json
   {
     "domain": "POC",
     "severity": 2,
     "scratchpad": {
       "sp1": "Concise answer to scratchpad question 1",
       "sp2": "Concise answer to scratchpad question 2",
       // ... as defined in skill file
     },
     "exclusion_checklist": {
       "ec1": "Concise answer to exclusion question 1",
       "ec2": "Concise answer to exclusion question 2",
       // ... as defined in skill file
     },
     "rationale": "Detailed explanation of why this score was assigned. Include specific examples from the study excerpt to support your evaluation. The target audience for this explanation is the provider who will be assessing the patient, so use clear, clinically precise language that emphasizes actionable insights and aligns with medical evaluation protocols."
   }
   ```

**After all flagged domains evaluated by subagents:**

4. **Main agent synthesizes results**:
   - Collect all subagent evaluations
   - Assign score 0 to all non-flagged domains (they were confirmed absent in Stage 1)
   - **WAIT until all domains have scores** before proceeding

5. **Write comprehensive rationale object**:

The `rationale` object must contain detailed, clinically-oriented explanations for:
- Each domain with severity score > 0
- Each flagged domain scored 0 (explain why absent despite initial concern)

**Each rationale entry should be 1 paragraph (2-4 sentences) that:**
- References specific words, phrases, or patterns from the study excerpt
- Explains what linguistic/thought features determined the FTD presence
- Justifies the specific severity level (why this score vs. higher or lower)
- Uses clinically precise language suitable for provider review
- Provides actionable insights for clinical assessment

Target audience: Healthcare providers conducting patient evaluations.

6. **Compile final output record** with all fields

## Subagent Deployment Strategy

**Why use subagents?**
- Each FTD evaluation gets independent context window
- Prevents cross-contamination between domain assessments
- Each subagent only loads its specific skill file
- Clean separation of diagnostic concerns

**How to deploy subagents:**
1. For each flagged FTD, conceptually create a "fresh" evaluation context
2. The subagent reads only its assigned skill file
3. The subagent focuses exclusively on that one FTD domain
4. Main agent collects and synthesizes all subagent results

**Important**: Execute subagent evaluations in parallel to treat each as independent with its own "mental space" for evaluation.


## Output Format Requirements

**For each intervention, write ONE line to output.jsonl with this exact structure:**

```json
{
  "id": "40010_fu1_tran_0059",
  "screening": {
    "decision": "needs_analysis",
    "flagged_ftds": ["POC", "TAN"],
    "screening_rationale": "Possible poverty of content with vague language; potential tangential drift"
  },
  "CIR": 0,
  "CLA": 0,
  "CON": 0,
  "DER": 0,
  "DOT": 0,
  "ECH": 0,
  "MAN": 0,
  "NEO": 0,
  "PER": 0,
  "POC": 2,
  "POS": 0,
  "POT": 0,
  "RES": 0,
  "SEM": 0,
  "TAN": 0,
  "VER": 0,
  "rationale": {
  "POC": "The patient's response demonstrates poverty of content of speech at a mild-to-moderate level (score 2). While the utterance is adequate in length, the informational density is significantly reduced due to excessive use of filler words ('um', 'well', 'like', 'you know', 'I guess', 'and stuff') which constitute approximately 50% of the speech content. The patient names only two subjects ('science and math') without elaboration, specification, or meaningful detail about what aspects are enjoyable or why they are favorites. The vague qualifier 'and stuff' suggests difficulty articulating concrete thoughts. This score of 2 reflects that the vagueness occurs several times within a single short response but does not render communication completely empty, distinguishing it from more severe presentations (3-4) where responses would be predominantly void of content.",
  "TAN": "No tangentiality detected (score 0). The patient maintains direct topical coherence throughout the response, addressing the specific question about favorite school subjects without deviation. Both mentioned subjects (science, math) are appropriate, on-topic responses to the interviewer's question. There is no drift toward unrelated themes, no gradual topic shift, and the patient does not introduce peripheral associations. The response, while vague in content (see POC), remains consistently focused on the academic subject matter requested, meeting the exclusion criteria for tangentiality."
},
  "scratchpad": {
    "POC": {
      "sp1": "Logical connection present between sentences",
      "sp2": "Does not employ idiosyncratic reasoning",
      "sp3": "No contradictions present"
    },
    "TAN": {
      "sp1": "Response addresses school subjects as asked",
      "sp2": "No drift away from topic"
    }
  },
  "exclusion_checklist": {
    "POC": {
      "ec1": "Yes - logical connections recognizable",
      "ec2": "Yes - follows consistent internal logic"
    },
    "TAN": {
      "ec1": "Yes - stays on topic throughout"
    }
  },
  "analyzed_at": "2025-11-17T10:30:00"
}
```

**Critical field requirements:**
- All 16 domain codes (CIR, CLA, CON, DER, DOT, ECH, MAN, NEO, PER, POC, POS, POT, RES, SEM, TAN, VER) with scores 0-4
- `screening` object with decision, flagged_ftds, screening_rationale
- `rationale` object with explanations for scored domains and flagged domains
- `scratchpad` object with entries ONLY for flagged domains
- `exclusion_checklist` object with entries ONLY for flagged domains
- `analyzed_at` timestamp in ISO 8601 format

## Workflow: Step-by-Step Execution

### Initialization
```
1. Read full transcript: results/{TRANSCRIPT_NAME}/transcription.md
2. Load input file: results/{TRANSCRIPT_NAME}/input.jsonl
3. Create/open output file: results/{TRANSCRIPT_NAME}/output_sonnet45.jsonl (write mode)
```

### For Each Line in input.jsonl (Sequential Processing)

```
4. Parse intervention record (id, line_number, close_context, study_excerpt)

5. STAGE 1: Initial Screening
   - Review study_excerpt with close_context
   - Apply one-liner definitions
   - Decide: everything_looks_good OR needs_analysis
   - If needs_analysis: identify specific FTD codes to flag
   - Record screening results

6. STAGE 2: Detailed Analysis (only if needs_analysis)
   For each flagged FTD:
     a. Deploy subagent for this domain
     b. Subagent reads skills/{FTD_CODE}/SKILL.md
     c. Subagent evaluates: scratchpad, exclusion checklist, severity score
     d. Subagent returns: score, scratchpad, exclusion_checklist, rationale

   Collect all subagent results

7. Result Synthesis
   - Compile all 16 domain scores (subagent scores + zeros for non-flagged)
   - WAIT until all 16 domains scored
   - Write rationale object (scored domains + flagged domains)
   - Compile scratchpad and exclusion_checklist (flagged domains only)
   - Add screening object and timestamp

8. Write Output
   - Append complete JSON record to output.jsonl (one line)
   - Ensure proper JSON formatting (no newlines within record)

9. Repeat for next intervention
```

### Post-Processing

```
10. After all interventions processed:
    - Read skills/format_validation/SKILL.md
    - Validate complete output.jsonl
    - Check: completeness, score validity, domain coverage, rationale completeness
    - Report validation results
```

## Validation Requirements

After processing all interventions, validate output.jsonl:

**Required checks:**
- [ ] All input IDs have corresponding output records
- [ ] No duplicate IDs in output
- [ ] All severity scores are integers in range [0-4]
- [ ] All 16 TALD domain codes present in every output record
- [ ] Every record has non-empty screening object
- [ ] Every record has rationale object with entries for scored/flagged domains
- [ ] Scratchpad entries present only for flagged domains
- [ ] Exclusion_checklist entries present only for flagged domains
- [ ] All timestamps are valid ISO 8601 format
- [ ] Each line is valid JSON

**Use the format_validation skill** (`skills/format_validation/SKILL.md`) for validation code snippets and detailed checking procedures.

## Critical Reminders

1. **READ THE FULL TRANSCRIPT FIRST** - Before analyzing any intervention, read the complete transcript file

2. **Stage 1 never concludes FTD present** - Only flag potential FTDs for Stage 2 confirmation

3. **Wait for all scores before rationale** - Do not write rationale until all 16 domains have been scored

4. **Subagent independence** - Each FTD evaluation should be independent with its own skill file

5. **Rationale detail and clinical precision** - Write 2-4 sentence paragraphs for each rationale entry that:
   - Quote specific text from study excerpt as evidence
   - Justify the exact severity score with reference to criteria
   - Use clinically precise language for provider assessment
   - Explain flagged-but-absent domains thoroughly

6. **Context escalation** - Use full transcript when patterns require broader context

7. **One line per output** - Each JSON record must be a single line in output.jsonl

8. **DON'T CONCLUDE THE TASK UNTIL EVERY INSTANCE OF THE TRANSCRIPT HAVE BEEN PROCESSED**

8. **Validate at the end** - Use format_validation skill to check complete output

## Begin Analysis

Start by:
1. Reading the full transcript: `results/{TRANSCRIPT_NAME}/transcription.md`
2. Loading the input file: `results/{TRANSCRIPT_NAME}/input.jsonl`
3. Processing interventions sequentially using the two-stage process
4. Writing results to: `results/{TRANSCRIPT_NAME}/output_sonnet45.jsonl`

Proceed systematically and thoroughly. Take your time with each evaluation. Good luck!