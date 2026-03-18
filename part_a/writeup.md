# Part A — Data Cleaning & Quality Analysis Writeup

## 1. Assumptions Made During Cleaning

* Conversations with fewer than 2 turns were removed, as they do not represent meaningful interaction between agent and customer.
* Empty or whitespace-only text in any turn was considered invalid, since such data is not useful for training conversational models.
* Negative call durations and missing outcomes were treated as invalid metadata and led to rejection of the conversation.
* Duplicate consecutive turns (same speaker and same text) were considered noise and removed to avoid redundancy in training data.
* Garbled or corrupted text (e.g., special characters like @@@###) was treated as unusable and filtered out.
* Language mismatch was handled using simple keyword-based heuristics (e.g., Hindi words like "hai", English words like "pay"). Conversations failing this check were rejected.

---

## 2. Hardest Issue to Detect

The most challenging issue to detect programmatically was **language mismatch**.

* Since the dataset contains Hindi, Hinglish, and English, there is no strict boundary between them.
* I used a simple keyword-based heuristic approach to approximate language detection.
* This method is not perfect, but it works reasonably well for small datasets and satisfies the assignment constraints.

---

## 3. Additional Checks Implemented

Beyond the required checks, I also ensured:

* Defensive coding using `.get()` to handle missing keys.
* Exception handling during JSON parsing to avoid script crashes.
* Modular validation functions for better readability and maintainability.

---

## 4. Scaling to Larger Dataset (100,000+ Conversations)

If the dataset size increases significantly, I would make the following improvements:

* **Use streaming processing** instead of loading everything into memory.
* **Introduce multiprocessing or parallel processing** to speed up validation.
* Store data in a **database or data lake (e.g., MongoDB, Parquet files)** instead of JSONL.
* Use more advanced **language detection libraries** instead of keyword heuristics.
* Build a **logging and monitoring system** to track data quality issues at scale.

---

## 5. Key Takeaways

* Real-world data is often messy and requires robust preprocessing.
* Writing clean, modular, and defensive code is critical for handling edge cases.
* Even simple heuristics can be effective when applied thoughtfully.
* Data quality directly impacts model performance, so this step is crucial before training any ML model.

---
