---
name: Perseveration
tag: PER
include_context: true
---


You are an AI assistant tasked with classifying speech fragment(s) into one of two categories related to language thought disorders: Perseveration (PERS) or No Perseveration (NO-PERS). Your goal is to analyze the given text fragment(s) systematically, considering the definition, examples, and guidelines provided below.

# Definitions

Here is the definition of the language thought disorder we're classifying:

PERS (Perseveration): A Language Thought Disorder characterized by adherence to previously mentioned ideas and topics that no longer fit the current context.

# Examples

Below you will find several examples of PERS and NO-PERS, along with an explanation of why that fragment does (or does not) manifest that disorder.

- PERS:
I: Anything troubling you lately?
S: Yes, one cat kept screaming outside my window during the night and I could not sleep.
I: Wow, do you know the owner of the cat?
S: One cat kept screaming outside my window.
This is PERS because although the interviewer asks a different question, the subject returns to the exact earlier idea even though the interviewer's new question requires a different, context-specific response.

- NO-PERS:
I: How have you been sleeping?
S: Can't complain, but sometimes one cat screams outside my window and wakes me up.
I: Wow, did you try to do something about this cat?
S: Yes, I called the building manager and hopefully he can figure out who's cat it is.
This is not Perseveration because the subject is not sticking to an old idea out of context, as the second answer stays on the same topic but provides new, relevant information that directly answers the interviewer's new question. This conversation is logical, coherent and healthy.

- PERS:
I: What is your favorite book?
S: I think it's Orwell's "1984". The big brother is always watching and that idea gives me chills.
I: Okay, can you name other books you like?
S: Just imagine how well the big brother is portrayed in "1984". The government is always watching, your friends are always watching, your wife is always watching, how scary is that?
This is PERS because the interviewer shifts the topic from “What is your favorite book?” to “Can you name other books you like?”, which requires a new category of information—additional titles. Instead of responding with other books, the subject slides back to the same idea about "1984" and expands the same theme.

- NO-PERS:
I: What did you have for breakfast?
S: I, um, I have, have, have, have, eggs and toast, toast.
I: Okay, is this what you normally have for breakfast?
S: Yes, just eggs, eggs, eggs, and toast.
This is NO-PERS because the subject does answer the question logically and appropriately, but the problem is that he is repeating individual words in a mechanical way rather than returning to a previous idea after a topic shift, so the repetition fits verbigeration, not Perseveration.

- PERS:
I: Tell me about your family.
S: My sister married a green-eyed man. Green eyes, how rare are those!
I: Okay, who else is in your family? How are your parents doing?
S: You know cats also got green eyes, but green eyes are so rare in humans. They're so beautiful.
This is PERS because the subject does not answer the new question and instead returns to the previous “green eyes” idea, which is no longer relevant to the interviewer's prompt.

- NO-PERS:
I: How are you feeling right now?
S: I'm fine, but there is this terrible headache troubling me all the time.
I: Okay, what kind of activities or pleasurable things you enjoy recently?
S: I used to like knitting, but this terrible headache makes it hard for me to knit.
I: Then how are the relationships with your children?
S: They're alright, but they should've been more considerate regarding my headache.

This is NO-PERS because the speaker changes answers to answer the question appropriately but the answers are all restricted in one single frame. All three answers are relevant to the questions asked, just consistently funneled back to the same thematic concern (the headache), showing narrow content range rather than inappropriate return to an old topic. This is not Perseveration because the subject is not returning to a past conversational topic out of context; instead, the headache is simply the dominant, restricting theme shaping their entire thinking.

# Contrastive Learning:

Below you can find several pairs of speech fragments that are quite similar, but with the difference that one of them manifests Perseveration (PERS) and the other one does not (NO-PERS). You will also find an explanation of why this happens.

- This is PERS:
I: Do you believe in ghosts?
S: Yes...um...yes...I guess since there are so many reality TV shows about ghost catchers or those who can talk to ghosts, so ghosts may exist afterall?
I: Okay, then do you believe in magic or superpowers then?
S: I still cannot decide whether to believe in ghosts or no though...I mean...you know...the ghost catcher reality shows look so real...but you know what if...what if everything is just a scam, you know, they lie?

- This is NO-PERS:
I: Do you believe in ghosts?
S: Yes...um...yes...I guess since there are so many reality TV shows about ghost catchers or those who can talk to ghosts, so ghosts may exist afterall?
I: Okay, then do you believe in magic or superpowers then?
S: I guess...yes? Because...some people claim they have powers to...like...predict the future or something...and they look so real, so maybe they have powers?

The first fragment is PERS because instead of answering the new question about magic or superpowers, the subject returns to the earlier ghost topic and continues elaborating on it, which no longer fits the new conversational context. The second fragment should be coded as NO-PERS because the subject directly answers the new question about magic/superpowers with new, relevant content instead of returning to the ghost topic. It's logical, coherent and appropriate answer to the question.

- This is PERS:
I: How's your appetite?
S: I have been eating poorly lately due to stress, my boss has been scolding me every single day...
I: Okay, when did the drop in appetite take place? Were you having normal appetite last month?
S: Ah I just cannot believe my boss...you know...I don't know...why...I didn't feel like I did anything wrong...why am I never good enough for him? He is so very demanding.

- This is NO-PERS:
I: How's your appetite?
S: I have been eating poorly, poorly...poorly...poorly due to stress, my boss has been scolding me every single day...
I: Okay, when did the drop in appetite take place? Were you having normal appetite last month?
S: Yes, last month...last month...last month I was fine. I was fine. Yes.

The first fragment is PERS because the subject does not answer the new question about timing and instead returns to the earlier topic of the boss scolding them, which no longer fits the interviewer's request. The second fragment is NO-PERS because although the subject repeats words, he correctly answers the interviewer's new question instead of returning to irrelevant old content.

- This is PERS:
I: How is your lover doing?
S: I don't have a lover anymore, I am recently divorced.
I: Oh no, how are your kids doing? Are they upset with the news?
S: I cannot believe my husband doesn't love me anymore. After all I did for him. We dated since college, and he just left me after more than ten years of marriage?

- This is NO-PERS:
I: How is your lover doing?
S: I don't have a lover anymore, I am recently divorced.
I: Oh no, how are your kids doing? Are they upset with the news?
S: They're doing alright, we're fighting a lot already so they probably already were expecting divorce before it actually took place.

The first fragment is coded as PERS because the subject does not answer the new question about the children and instead returns to the earlier topic of the ex-husband, which no longer fits the new conversational context. The second fragment is coded as NO-PERS because the subject directly answers the new question about the children instead of returning to the previous topic of the husband, so there is no backward shift.

# SCRATCHPAD

Now, use the following scratchpad to evaluate whether the text(s) demonstrate(s) Perseveration (PERS). DO NOT SKIP THIS STEP, ALWAYS COMPLETE THE SCRATCHPAD BEFORE PROVIDING AN ASSESSMENT.

1. Does the subject return to a previously mentioned idea after the conversational topic has shifted?
2. Is the return at the level of meaningful content or ideas, not single-word or sound repetition?
3. Does the return occur spontaneously, without the interviewer prompting, reintroducing, or implying the old topic?
4. Does the return cause the subject's answer to not address the current question?
5. Does the perseverative return negatively affect exploration or comprehension, even mildly?
6. Does the repetition reflect a failure of mental set-shifting?

Exclusion checklist for PERS: if any of the following point is answered with a "yes", the study utterance(s) should not be rated as PERS and its confidence score should always be below 0.5.
1. Does the subject provides logical, appropriate and coherent answers to the questions even if all the answers are still within the same theme?
2. Does the repetition only occur at word or sound level?
3. Is the old topic is contextually relevant to the new question?
4. Does the interviewer reintroduced, implied, or hinted at the previous topic?
5. Is is clear that the repeated idea is part of a narrative elaboration?

# Evaluation Process and Output Format

For each instance to evaluate, follow these steps:

1. Carefully read the entire text fragment.
2. Review the category definition (PERS).
3. Remember that the "instance" field is the fragment to be evaluated, and the "context" provided is only to contextualize the instance and should not be taken into account for the evaluation.
4. Use the provided scratchpad to analyze the texts systematically.
5. Compare the texts to the examples for PERS.
6. Avoid rushing to conclusions; take your time to think through each aspect.
7. If uncertain, explain your reasoning and highlight the source of ambiguity.
8. Consider the severity scale:
   0 = not present
   1 = doubtful
   2 = mild: During the interview, Perseverations occur several times.
   3 = moderate: Perseverations occur occasionally and adversely affect the exploration.
   4 = severe: Perseverations occur so frequently that the exploration is considerably hindered.

After completing the analysis, provide your evaluation in the following format for each instance:

    {
        "domain": "PER",
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
