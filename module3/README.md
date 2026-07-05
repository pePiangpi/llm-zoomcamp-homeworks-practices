# Module 3 Homework - AI Orchestration with Kestra

This repository contains my solutions for Module 3 of the LLM Zoomcamp. 

## Methodology & Results

### Question 1: Context Engineering
*   **Action:** Compared prompt responses between ChatGPT and Kestra AI Copilot.
*   **Observation:** Kestra's AI Copilot provides more accurate and relevant flows because it has direct access to the Kestra plugin documentation.
*   **Answer:** AI Copilot has access to current Kestra plugin documentation.

### Question 2: RAG vs No RAG
*   **Action:** Executed `1_chat_without_rag.yaml` and `2_chat_with_rag.yaml` and compared execution logs.
*   **Observation:** The non-RAG version provided outdated/generic information about features, whereas the RAG version was grounded in actual release notes.
*   **Answer:** Vague, generic, or fabricated — the model guesses from training data.

### Questions 3 & 4: Token Usage (Short vs. Long Summary)
*   **Action:** Ran `4_simple_agent.yaml` with `summary_length` set to `short`, then `long`. Analyzed the `log_token_usage` task logs.
*   **Short Summary Result:** ~122 output tokens.
*   **Long Summary Result:** ~212 output tokens.
*   **Conclusion:** The long summary used 2-5x more tokens.

### Question 5: Modifying a flow
*   **Action:** Modified `4_simple_agent.yaml` in the Kestra flow editor. I updated the `english_brevity` task prompt from "exactly 1 sentence" to "exactly 3 sentences."
*   **Result:** Ran the flow with `summary_length = long`. Token usage was ~86 output tokens.
*   **Answer:** About the same (within 20%).

### Question 6: Best Practices
*   **Answer:** Use traditional task-based workflows for predictability and auditability.

---

## Repository Contents
- `1_chat_without_rag.yaml`
- `2_chat_with_rag.yaml`
- `4_simple_agent.yaml` (Modified: Contains the 3-sentence constraint change for Question 5)

---
*Completed as part of the DataTalksClub LLM Zoomcamp 2026.*