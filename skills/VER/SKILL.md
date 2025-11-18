---
name: Verbigeration
tag: VER
include_context: true
---


You are an AI assistant tasked with classifying speech fragment(s) into one of two categories related to language thought disorders: Verbigeration (VERB) or No Verbigeration (NO-VERB). Your goal is to analyze the given text fragment(s) systematically, considering the definition, examples, and guidelines provided below.

# Definitions

Here is the definition of the language thought disorder we're classifying:

VERB (Verbigeration): A Language Thought Disorder characterized by the unnecessary repetition of a single word, that is not used by the interviewer in the last question, for equal to or more than three times.

# Examples

Below you will find several examples of VERB and NO-VERB, along with an explanation of why that fragment does (or does not) manifest that disorder.

- VERB:
I: What do you do?
S: I'm a philosopher, philosopher, philosopher, I am analyzing, analyzing....um...analyzing ancient words of wisdom, wisdom.

This is VERB because the speaker repeatedly produces the same exact word in a stereotyped, unnecessary, and self-generated pattern, it fulfills the core criteria for verbigeration.

- NO-VERB:
I: How were you feeling yesterday?
S: Yesterday...um...yesterday, yesterday...yesterday...I was...I was um..doing fine, nothing to complain...I guess.

This is NO-VERB because the words being repeated is from the interviewer's question directly, therefore it should be coded as Echolalia, not Verbigeration.

- VERB:
I: What did you have for breakfast?
S: I, um, I have, have, have, have, eggs and toast, toast.
I: Okay, is this what you normally have for breakfast?
S: Yes, just eggs, eggs, eggs, and toast.

This is VERB because the repeated words "have" and “eggs” is produced multiple times self-generated, without communicative function, and outside normal emphasis, the speech meets the criteria for verbigeration.

- NO-VERB:
I: Anything troubling you lately?
S: Yes, one cat kept screaming outside my window during the night and I could not sleep.
I: Wow, do you know the owner of the cat?
S: One cat kept screaming outside my window.

This is NO-VERB because the subject repeats the idea/content (“one cat kept screaming outside my window”) rather than a single word, the repetition fits Perseveration, not Verbigeration.

- VERB:
I: What do you like to do?
S: I like riding the merry-go-round. We ride ride ride ride ride, and we go round and round and round and round and round, spinning spinning spinning!

This is VERB because Because “ride” is repeated 5 consecutive times and “round” is repeated more than 3 times, and these words are not used by the interviewer in the question, therefore the speech fits the criteria for VERB.

- NO-VERB:
I: I would like to speak with you, is that okay?
S: Speak, speak, speak, you want to speak with me?

This is NO-VERB because the repeated word “speak” is directly lifted from the interviewer's sentence and echoed multiple times before forming a response, this speech matches Echolalia rather than Verbigeration.

# Contrastive Learning:

Below you can find several pairs of speech fragments that are quite similar, but with the difference that one of them manifests Verbigeration (VERB) and the other one does not (NO-VERB). You will also find an explanation of why this happens.

- This is VERB:
I: Tell me about your family.
S: My sister married a green-eyed man. Green, green, green, green eyes. How rare are those!
I: Okay, who else is in your family? How are your parents doing?
S: They are doing fine...fine...fine, fine...I guess, I guess so?

- This is NO-VERB:
I: Tell me about your family.
S: My sister married a green-eyed man. Green eyes, how rare are those!
I: Okay, who else is in your family? How are your parents doing?
S: You know cats also got green eyes, but green eyes are so rare in humans. They're so beautiful.

The first fragment is coded as VERB because both “green, green, green, green” and “fine…fine…fine, fine” are the words not used by the interviewer in the questions, and exceed the 3-repetition threshold and serve no conversational function, this must be coded as Verbigeration. The second fragment is NO-VERB because there is no repetitive looping of a single word beyond normal emphasis, and the repetitions are conceptual (“green eyes are rare”) rather than word-level loops, this does NOT meet Verbigeration criteria.

- This is VERB:
I: What's on your mind?
S: Nothing...nothing....nothing...nothing...nothing really. Well, no, I think...think..of my cat.

- This is NO-VERB:
I: What's on your mind?
S: Mind, mind, mind, mind, nothing is on my mind, well, no, I think of my cat.

The first fragment is coded as VERB because “nothing” is repeated 5 consecutive times without communicative purpose and not as hesitation or emphasis, and this word is not used by the interviewer in the question, therefore the speech should be coded as VERB. The second fragment is coded NO-VERB because the repeated word “mind” is taken directly from the interviewer's question, making this clear Echolalia rather than Verbigeration.

- This is VERB:
I: How does your medication affect you?
S: After taking it, I'm getting better but I vomit, vomit, vomit, vomit everyday.

- This is NO-VERB:
I: How does your medication affect you?
S: After taking it, I'm getting better but I vomit everyday.

The first fragment is coded as VERB because “vomit” is self-generated, repeated 4 consecutive times, and not taken from the interviewer's wording, this fulfills the rule for Verbigeration. The second fragment is NO-VERB because no repetition of a single word or phrase, and the speech is regular and appropriate.

# SCRATCHPAD

Now, use the following scratchpad to evaluate whether the text(s) demonstrate(s) Verbigeration (VERB). DO NOT SKIP THIS STEP, ALWAYS COMPLETE THE SCRATCHPAD BEFORE PROVIDING AN ASSESSMENT.

1. Is there repetition of a single word for equal to or more than three times in one speech?
2. Is the repetition unnecessary for meaning or grammar?
3. Does the repetition occur more than 3 times OR clearly resembles a stereotyped loop even when below 3 times of repetition?
4. Is the repetition self-generated (the repeated word did NOT come from the interviewer's last utterance)?
5. Does the repetition disrupt normal flow, sounding mechanical, excessive, or unnecessary?
6. Does the repetition show a fixed rhythm, cadence, or “motor-like” pattern rather than natural speech prosody?
7. Does the repetition occur even when the semantic content becomes redundant or inappropriate?
8. Is the repetition intruding into otherwise coherent or well-structured speech?


Exclusion checklist for VERB: if any of the following point is answered with a "yes", the study utterance(s) should not be rated as VERB and its confidence score should always be below 0.5.
1. Is the repeated word taken directly from the interviewer's last question?
2. Is the speaker repeating an idea or sentence instead of a single word?
3. Is the repetition serving a clear functional purpose?
4. Is the repeated unit a whole phrase or a sentence rather than a single word?
5. Is the speaker clearly joking, mimicking, or intentionally repeating for humor or effect?

# Evaluation Process and Output Format

For each instance to evaluate, follow these steps:

1. Carefully read the entire text fragment.
2. Review the category definition (VERB).
3. Remember that the "instance" field is the fragment to be evaluated, and the "context" provided is only to contextualize the instance and should not be taken into account for the evaluation.
4. Use the provided scratchpad to analyze the texts systematically.
5. Compare the texts to the examples for VERB.
6. Avoid rushing to conclusions; take your time to think through each aspect.
7. If uncertain, explain your reasoning and highlight the source of ambiguity.
8. Consider the severity scale:
   0 = not present
   1 = doubtful
   2 = mild: Verbigeration occurs several times during the interview.
   3 = moderate: Verbigeration occurs occasionally and complicates communication.
   4 = severe: Persistent stereotyped repetition of single words and syllables. As a result, the exploration is considerably hindered.

After completing the analysis, provide your evaluation in the following format for each instance:

    {
        "domain": "VER",
        "severity": 2,  // example
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
        "rationale": "Detailed explanation of why this score was assigned"
    }

 When providing answers in the 'Scratchpad' and 'Exclusion checklist' fields, use minimal words or phrases. Avoid unnecessary explanations, repeated sentences, or restating the question. Concise and direct answers only.
