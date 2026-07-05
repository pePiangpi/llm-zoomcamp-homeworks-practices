# Module 3 Homework - AI Orchestration with Kestra

This repository contains my solutions for Module 3 of the LLM Zoomcamp. 

## Methodology & Results

### Question 1: Context Engineering
*   **Action:** Compared prompt responses between ChatGPT and Kestra AI Copilot. Used Kestra AI Copilot to generate the BigQuery source code file [zoomcamp.nyc_taxi_bq.yaml](zoomcamp.nyc_taxi_bq.yaml).
*   **Observation:** Kestra's AI Copilot provides more accurate and relevant flows because it has direct access to the Kestra plugin documentation.
*   **Answer:** AI Copilot has access to current Kestra plugin documentation.

### Question 2: RAG vs No RAG
*   **Action:** Executed [zoomcamp.1_chat_without_rag.yaml](zoomcamp.1_chat_without_rag.yaml) and [zoomcamp.2_chat_with_rag.yaml](zoomcamp.2_chat_with_rag.yaml) and compared execution logs.
*   **Observation:** The non-RAG version hallucinated that version 0.22.0 was released on May 13, 2024. The RAG version correctly identified that Kestra 1.1 was released on November 4, 2025.
*   **Answer:** Vague, generic, or fabricated — the model guesses from training data.

### Question 3: Token Usage (Short Summary)
*   **Action:** Ran [zoomcamp.4_simple_agent.yaml](zoomcamp.4_simple_agent.yaml) with `summary_length` set to `short`.
*   **Result:** Multilingual Agent output tokens = 80.
*   **Answer:** 60-100 tokens.

### Question 4: Token Usage (Long Summary)
*   **Action:** Ran [zoomcamp.4_simple_agent.yaml](zoomcamp.4_simple_agent.yaml) with `summary_length` set to `long`.
*   **Result:** Multilingual Agent output tokens = 163 .
*   **Conclusion:** 163 tokens is roughly 2x the short summary output of 80 tokens.
*   **Answer:** 2-5x more.

### Question 5: Modifying a Flow
*   **Action:** Modified [zoomcamp.4_simple_agent.yaml](zoomcamp.4_simple_agent.yaml) to update the `english_brevity` task prompt from "exactly 1 sentence" to "exactly 3 sentences."
*   **Result:** Ran the flow with `summary_length` set to `long`. English Brevity Agent output tokens increased from 55 to 84 tokens.
*   **Conclusion:** Expanding the prompt to 3 sentences scales up the token output, placing it in the 2-4x range compared to the 1-sentence baseline.
*   **Answer:** 2-4x more.

### Question 6: Best Practices
*   **Answer:** Use traditional task-based workflows for predictability and auditability.

---

## Repository Contents
- [zoomcamp.nyc_taxi_bq.yaml](zoomcamp.nyc_taxi_bq.yaml) (Created for Question 1)
- [zoomcamp.1_chat_without_rag.yaml](zoomcamp.1_chat_without_rag.yaml)
- [zoomcamp.2_chat_with_rag.yaml](zoomcamp.2_chat_with_rag.yaml) 
- [zoomcamp.3_vector_store.yaml](zoomcamp.3_vector_store.yaml)
- [zoomcamp.4_simple_agent.yaml](zoomcamp.4_simple_agent.yaml) (Modified with the 3-sentence constraint change for Question 5)
- [zoomcamp.5_subflow.yaml](zoomcamp.5_subflow.yaml)
- [zoomcamp.6_multi_agent_research.yaml](zoomcamp.6_multi_agent_research.yaml)


---
*Completed as Module3 of the DataTalksClub LLM Zoomcamp 2026.*