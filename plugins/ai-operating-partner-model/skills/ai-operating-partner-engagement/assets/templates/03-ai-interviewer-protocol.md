# AI Interviewer Operating Protocol

`protocol_id`: `ai_interviewer_protocol`
`status`: `published_reference`
`applies_to_step`: `3`

This protocol makes AI-led interviews shippable in enterprise settings. It is the operating contract for participant trust, consent, recording, redaction, intervention, refusal fallback, and interview quality.

## 1. Hosting And Data Boundary

- The interview environment, transcript storage, and retention location must be named before interviews begin.
- If the client has data-residency, legal, privacy, or vendor-review requirements, Step 0 must record them and Step 3 must honor them.
- The interviewer must not request credentials, live system access, screenshots, uploads, all-email access, or production data during the interview.
- Participants may describe artifacts; evidence requests are captured silently and handled later in Step 5.

## 2. Consent And Participant Notice

Before the interview starts, the participant must receive a short notice covering:

- purpose of the interview;
- whether audio, transcript, or summary is retained;
- who can see the transcript or summary;
- retention period or deletion policy;
- no live upload or credential request;
- how to correct the interviewer;
- how to refuse a question or stop.

The participant must affirm consent before the interview continues.

## 3. Recording, Transcription, And Retention

- Default mode is transcript or structured summary, not raw audio retention.
- Raw audio retention must be explicitly approved by the client.
- Transcript retention must follow the Step 0 scope and any client legal/security requirement.
- Sensitive information should be summarized into classified fields where possible instead of copied verbatim.
- Raw transcripts should not be included in client-facing product views unless the client explicitly approves.

## 4. Redaction Before Structured Use

Before transcript content is promoted into the workflow intelligence object:

- redact or classify unnecessary PII, financial account details, credentials, secrets, personal health details, and other sensitive values;
- preserve evidence references and content class even when raw values are removed;
- record redaction status on evidence references;
- route unresolved sensitivity questions to Step 8 validation or Step 15 risk/control.

## 4a. Live Sensitive Disclosure Handling

If a participant volunteers PII, financial account details, credentials, secrets, personal health details, protected-class signals about other employees or third parties, or other sensitive values during the live interview, the interviewer must:

- pause and acknowledge that the disclosure was unsolicited;
- not request or repeat the sensitive value;
- not retain the verbatim value in transcripts, summaries, or worked notes;
- summarize the relevant content into a classified field (e.g., "credential disclosed for system X" rather than the credential itself, or "protected-class signal raised about a named individual" rather than the signal itself);
- log the moment as a sensitivity event with timestamp, content class, and routing decision;
- route the event to Step 8 governance resolution, Step 15 risk/control, or both, depending on whether it concerns access posture, output risk, or a third party;
- when credentials or live-system access are volunteered, remind the participant that the engagement does not request or use credentials and that the value will not be retained.

The interviewer must never treat unsolicited disclosure as authorization to expand scope. The redaction queue handles the artifact; Step 5 follow-up may revisit the underlying need only after operator review.

## 5. No Asserted Org Facts

The AI interviewer may ask, summarize, and confirm. It must not assert facts about the organization unless the participant already stated them in the same interview.

Allowed:

- "I heard you say the invoice is checked in Yardi and then compared to an Excel tracker. Is that right?"
- "Who usually knows whether that adjustment is final?"

Not allowed:

- "Your team uses Yardi as the official source."
- "The tracker is unreliable."

## 6. Follow-Up Correction Protocol

If the AI misunderstands a term, role, source, or rule:

1. participant correction is accepted without argument;
2. corrected term is restated back;
3. original misunderstanding is marked as superseded;
4. if the correction affects a material source, decision, or truth chain, it is flagged for Step 6 object construction and Step 8 validation.

## 7. Operating Partner Intervention

The operating partner may intervene when:

- participant trust is at risk;
- the AI asks a confusing or leading question;
- the AI appears to assert unvalidated org facts;
- the participant shares sensitive data that should be stopped or redirected;
- coverage is drifting away from the candidate use case;
- a senior or skeptical participant needs human facilitation;
- the interview reveals a material risk that should not be explored further without client approval.

Interventions should be logged as interview-quality events.

## 8. Refusal And Fallback

If a participant refuses an AI-led interview:

- offer a human-led interview using the same question structure;
- offer asynchronous written response if appropriate;
- allow a shorter executive or senior-operator interview with targeted prompts;
- record participation bias and coverage gap in Step 4 if the refusal affects representativeness.

Refusal must not be treated as non-cooperation. It is a sampling and adoption signal.

## 9. Synchronous And Asynchronous Norms

- Default operator interviews: 30-45 minutes synchronous.
- Senior executive or high-skepticism interviews: 20-30 minutes, human-facilitated if needed.
- Asynchronous interviews: use only for factual collection, not for nuanced tacit judgment, politics, or sensitive edge cases.
- Follow-up clarification: 5-10 targeted questions maximum unless the operating partner approves more.

## 10. Quality And Coverage Checks

Every interview batch should produce:

- role and layer coverage;
- participation skew;
- work episodes captured;
- edge cases captured;
- source access paths captured;
- truth production signals captured;
- adoption signals captured;
- silent evidence needs;
- confidence and quality score;
- unresolved follow-up questions.

The batch is not complete when only generic opinions are captured. It needs recent real work episodes.
