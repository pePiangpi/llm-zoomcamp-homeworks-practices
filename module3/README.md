# Module 3 Homework - AI Orchestration with Kestra

This repository contains my solutions for Module 3 of the LLM Zoomcamp. 

## Methodology & Results

### Question 1: Context Engineering
*   **Action:** Compared prompt responses between ChatGPT and Kestra AI Copilot. Used Kestra AI Copilot to generate the BigQuery source code file (`nyc_taxi_bq.yaml`).
*   **Observation:** Kestra's AI Copilot provides more accurate and relevant flows because it has direct access to the Kestra plugin documentation.
*   **Answer:** AI Copilot has access to current Kestra plugin documentation.

### Question 2: RAG vs No RAG
*   **Action:** Executed `1_chat_without_rag.yaml` and `2_chat_with_rag.yaml` and compared execution logs.
*   **Observation:** The non-RAG version hallucinated that version 0.22.0 was released on March 20, 2024[cite: 1]. The RAG version correctly identified that Kestra 1.1 was released on November 4, 2025[cite: 1].
*   **Answer:** Vague, generic, or fabricated — the model guesses from training data.

### Question 3: Token Usage (Short Summary)
*   **Action:** Ran `4_simple_agent.yaml` with `summary_length` set to `short`[cite: 1].
*   **Result:** Multilingual Agent output tokens = 80[cite: 1].
*   **Answer:** 60-100 tokens.

### Question 4: Token Usage (Long Summary)
*   **Action:** Ran `4_simple_agent.yaml` with `summary_length` set to `long`[cite: 1].
*   **Result:** Multilingual Agent output tokens = 163[cite: 1].
*   **Conclusion:** 163 tokens is roughly 2x the short summary output of 80 tokens[cite: 1].
*   **Answer:** 2-5x more.

### Question 5: Modifying a Flow
*   **Action:** Modified `4_simple_agent.yaml` to update the `english_brevity` task prompt from "exactly 1 sentence" to "exactly 3 sentences."
*   **Result:** Ran the flow with `summary_length` set to `long`[cite: 1]. English Brevity Agent output tokens increased from 55 to 84 tokens[cite: 1].
*   **Conclusion:** Expanding the prompt to 3 sentences scales up the token output, placing it in the 2-4x range compared to the 1-sentence baseline.
*   **Answer:** 2-4x more.

### Question 6: Best Practices
*   **Answer:** Use traditional task-based workflows for predictability and auditability.

---

## Repository Contents
- `nyc_taxi_bg.yml` (Created for Question 1)
- `1_chat_without_rag.yaml`
- `2_chat_with_rag.yaml`
- `3_rag_with_websearch.yaml`
- `4_simple_agent.yaml` (Modified with the 3-sentence constraint change for Question 5)
- `5_web_research_agent.yaml`
- `6_multi_agent_research.yaml`

---
*Completed as part of the DataTalksClub LLM Zoomcamp 2026.*