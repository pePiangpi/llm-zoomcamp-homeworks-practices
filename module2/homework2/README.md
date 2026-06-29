# Module 2: Vector Search

In this module, we extend the RAG pipeline from Module 1 by introducing **Vector Search**. While traditional keyword search relies on exact token overlap, vector search matches documents based on their deep semantic meaning. 

We will cover everything from the mathematical foundations of text embeddings to implementing persistent, production-ready vector databases and lightweight ONNX-based execution runtimes.

---

## 📂 Directory Structure

* `code/` — Practical notebook implementations, homework scripts, and step-by-step lab exercises.
* `embed/` — Configuration scripts and local models for the embedding execution runtimes.

---

## 📚 Syllabus & Lessons

The curriculum covers vector search end-to-end, moving from basic in-memory math to persistent data stores:

1.  **What is Vector Search** — Comparing exact keyword search vs. semantic vector search and understanding why context matters.
2.  **Embeddings** — Deep dive into turning text strings into dense numerical vectors using `sentence-transformers`.
3.  **Embedding Our Dataset** — Generating and optimizing embeddings for our custom FAQ dataset.
4.  **Vector Search with NumPy** — Building a baseline search mechanism completely from scratch using raw matrix operations (`np.dot` / cosine similarity).
5.  **Vector Search with minsearch** — Implementing efficient, in-memory vector search capabilities using the localized utility search library.
6.  **RAG with Vector Search** — Upgrading our RAG pipeline by swapping out lexical retrieval for semantic vector retrieval.
7.  **Vector Search with sqlitesearch** — Building persistent, file-backed vector stores utilizing an SQLite engine wrapper.
8.  **Vector Search with PGVector** — Setting up production-grade vector search stacks using PostgreSQL and the `pgvector` extension.
9.  **ONNX Embedder (Optional)** — Compiling models to ONNX Runtime for lightweight, high-performance CPU inference without a heavy PyTorch footprint.
10. **Next Steps** — Architecture evaluation: choosing between keyword, vector, and hybrid search pipelines.

---

## 📝 Homework

Complete the tracking assignments found in the [Homework](./homework/) directory to solidify your understanding of cosine similarity mechanics, indexing workflows, and hybrid Reciprocal Rank Fusion (RRF) alignments.

---
