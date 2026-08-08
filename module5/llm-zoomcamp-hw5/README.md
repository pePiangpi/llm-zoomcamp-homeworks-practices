# Module 5: Monitoring & Observability

Welcome to my implementation for **Module 5: Monitoring** of the [DataTalks.Club LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) course. This module focuses on tracking, monitoring, and debugging production-grade Retrieval-Augmented Generation (RAG) applications using **OpenTelemetry (OTel)** and custom span exporters rather than relying solely on black-box logging.

---

## 🚀 What I Learned & Implemented

* **OpenTelemetry Instrumentation:** Integrated OTel tracing directly into a custom RAG pipeline to capture execution spans, request durations, and internal tool execution flows.
* **Span Attributes & Metrics:** Tracked critical performance indicators such as `input_tokens`, `output_tokens`, and system latency directly as structured span attributes.
* **Custom SQLite Exporter:** Built a local SQLite exporter from the ground up to intercept, store, and query trace data locally (`traces.db`) without requiring heavy, external monitoring backends.
* **Trace Analysis & Dashboarding:** Loaded trace logs into [Pandas](https://pandas.pydata.org/) to inspect system consistency, verify token stability across multiple model invocations, and analyze overall pipeline reliability.

---

## 📂 File Directory Structure

* **[`traces.db`](./traces.db)** — The local SQLite database storing captured execution traces, span names, timing metrics, and input token counts.
* **`starter.py` / Application Scripts** — Python scripts executing the RAG flow, handling OpenTelemetry setup, and recording data to the local exporter.
* **`q6_check_tokens.py`** — Data analysis script utilizing Pandas to verify token stability across multiple automated runs.

---

## 🔗 Course & Community Links

* Course Main Repository: [DataTalksClub/llm-zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp)
* Official Course Documentation: [DataTalks.Club LLM Zoomcamp Docs](https://datatalks.club/docs/courses/llm-zoomcamp/)
* Course Homework Submission Portal: [LLM Zoomcamp Homework Platform](https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw5)