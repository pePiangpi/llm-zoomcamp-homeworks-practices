# LLM Zoomcamp: Homework & Projects

This is my personal workspace for the DataTalksClub LLM Zoomcamp course. It contains my homework assignments, practice code, and hands-on experiments for building production-ready LLM and RAG applications.

## 📁 Repository Structure

* **[`module1/`](./module1/)** — All assignments, local scripts, and notebooks for structural Retrieval-Augmented Generation (RAG).
  * [`homework1/`](./module1/homework1/homework1.ipynb) — Dedicated folder containing Module 1 assignment and evaluation notebooks.
* **[`module2/`](./module2/)** — Semantic Retrieval and Vector Indexing implementations.
  * [`homework2/`](./module2/homework2/homework2.ipynb) — Dedicated folder containing Module 2 assignment and evaluation notebooks.
  * `*.ipynb` — Step-by-step lesson notebooks covering semantic search, embedding generation, and databases like PGVector.
* **[`pyproject.toml`](./pyproject.toml)** — Global project configuration file managing dependencies using `uv`.
* **[`module3/`](./module3/)** — Workflow automation, task pipelines, and AI orchestration using Kestra.
  * — Dedicated folder containing Module 3 assignment workflows and execution logs.
  * `*.yaml` — Step-by-step pipeline configurations covering context engineering, RAG validation, and agent token tracking. 
* **[`module4/`](./module4/)** — Testing and improving search performance. This module implements a rigorous evaluation framework to measure search accuracy using metrics like Hit Rate and Mean Reciprocal Rank (MRR). It covers ground truth construction, Reciprocal Rank Fusion (RRF) tuning, and systematic performance testing to replace manual guesswork.
  * [`homework4/`](./module4/homework4/homework4.ipynb) — Contains the hands-on evaluation notebooks, datasets, and experiment logs generated during the testing process.
* **[`module5/`](./module5/)** — Monitoring and observability. Implements OpenTelemetry (OTel) instrumentation for RAG pipelines, capturing tokens and latencies as span attributes, and building a custom SQLite span exporter and trace analysis dashboard.
  * [`traces.db`](./module5/llm-zoomcamp-hw5/traces.db) — SQLite database recording execution spans, tool calls, and token metrics.
  
pyproject.toml — File that manages all the project tools and versions.


## 🛠️ Tech Stack

* **Language:** Python
* **Package Manager:** `uv` (Managing global workspace dependencies)
* **Orchestration & Workflow:** Kestra (Automated task pipelines & LLM orchestration)
* **Containerization:** Docker (Local environment & pipeline deployment)
* **Search Engine & Retrieval:** `minsearch` (In-memory Lexical & Vector search)
* **Vector Databases & Storage:** PostgreSQL with `pgvector`, SQLite (`sqlitesearch`)
* **Embeddings & Inference:** `sentence-transformers`, ONNX Runtime (CPU-optimized inference)
* **LLM Orchestration:** Custom RAG pipelines & Hybrid Search (Reciprocal Rank Fusion)
* **Evaluation & Metrics:** Hit Rate, Mean Reciprocal Rank (MRR), and Ground Truth performance benchmarking
* **Observability & Monitoring:** OpenTelemetry (OTel), Custom SQLite Exporters, Span Tracing, Token & Latency Tracking


## 📝 Course & Homework Tracking

* **Module 1: Agentic RAG** — Introduction to RAG, token counting, and basic retrieval
  * [✅] [Homework 1](module1/homework1/homework1.ipynb)
* **Module 2: Vector Search** — Semantic search with embeddings, PGVector, and minsearch
  * [✅] [Homework 2](module2/homework2/homework2.ipynb)
* **Module 3: Orchestration** — AI orchestration pipelines using Kestra
  * [✅] [Homework 3](module3)
* **Module 4: Evaluation** — Measuring retrieval and answer quality using LLM-as-a-Judge
  * [✅] [Homework 4](module4/homework4/homework4.ipynb)
* **Module 5: Monitoring** — Tracking user feedback and system health with live dashboards
  * [✅] [Homework 5](module5/llm-zoomcamp-hw5/homework5.py)
* **Module 6: Best Practices** — Hybrid search (vector + keyword) and reranking techniques
  * [ ] Homework 6 *(Coming Soon)*
* **Module 7: End-to-End Project** — Implementing a complete fitness assistant workflow
  * [ ] Project Phase *(Coming Soon)*
* **Capstone Project** — Building, evaluating, and shipping my own complete RAG application
  * [ ] Final Capstone *(Coming Soon)*

---

*This repository is updated as the course progresses through each module.*
