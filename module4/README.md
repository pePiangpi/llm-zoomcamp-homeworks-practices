# Module 4: RAG Evaluation & Performance Tuning

In this module, we transition from building RAG systems to measuring their actual performance. While development focuses on implementation, evaluation focuses on accuracy, reliability, and precision. We move away from manual "guessing" and implement rigorous frameworks to quantify search relevance, optimize search parameters, and validate system quality through data-driven testing.

---

## 📂 Directory Structure

* [`homework4/`](./homework4/homework4.ipynb) — Dedicated folder containing my Module 4 homework and evaluation notebooks.
* `*.ipynb` — Step-by-step lesson notebooks covering evaluation metrics, RAG assessment, and search optimization.

---

## 📚 Syllabus & Lessons

The curriculum covers the full evaluation lifecycle, moving from defining success metrics to systematic performance tuning:

1.  **The Case for Evaluation** — Understanding why qualitative "gut feel" is insufficient and why we need quantitative metrics.
2.  **Core Metrics** — Implementing and calculating **Hit Rate** and **Mean Reciprocal Rank (MRR)** to score retrieval success.
3.  **Building Ground Truth** — Constructing reliable test datasets (questions and corresponding relevant document IDs) to establish a fair benchmark.
4.  **The Evaluation Framework** — Building a reusable `evaluate` function to test any search pipeline configuration instantly.
5.  **Tuning Keyword Search** — Optimizing field boosts (e.g., weighting `question` vs. `content`) to improve lexical relevance.
6.  **Optimizing Hybrid Search** — Experimenting with Reciprocal Rank Fusion (RRF) and tuning the `k` parameter for better ranking results.
7.  **Performance Benchmarking** — Running comparative A/B tests to see how configuration changes directly impact system metrics.
8.  **Data-Driven Decisions** — Using the evaluation pipeline to replace "guessing" with measurable, iterative improvements.

---

## 📝 Homework

Complete the tracking assignments found in the [`homework4/`](./homework4/homework4.ipynb) directory to solidify your understanding of metric calculation, parameter tuning, and search optimization workflows.