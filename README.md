# ML Intern Assignment — Kapture CX

This repository contains my solution for the ML Intern take-home assignment.

---

## 📌 Part A — Data Cleaning

* Generated 100 noisy EMI conversation datasets
* Implemented cleaning pipeline (`clean_data.py`)
* Filtered invalid data and created quality report
* Output: cleaned and rejected datasets

---

## 🤖 Part B — LLM Finetuning

* Fine-tuned **Qwen2.5-0.5B-Instruct** using LoRA
* Converted dataset into instruction format
* Trained model on Google Colab (T4 GPU)
* Evaluated responses using simple heuristics

---

## ⚙️ How to Run

### Part A:

```bash
cd part_a
python clean_data.py
python quality_report.py
```

### Part B:

* Open `part_b/finetune.ipynb` in Google Colab
* Upload `cleaned_conversations.jsonl`
* Run all cells

---

## 🔗 Colab Notebook

Colab Link: https://colab.research.google.com/drive/1gF0O1fjRQ3Wf10EocmQvAB1Wl-6sG9yv?usp=sharingcd

---

## ✅ Summary

End-to-end pipeline:
**Data Generation → Cleaning → Analysis → LLM Finetuning → Evaluation**

---
