# EMI Conversation Data Cleaning & LLM Fine-Tuning

An end-to-end machine learning project focused on cleaning noisy EMI-related conversations, analyzing data quality, and fine-tuning a small language model to generate relevant responses.

## Overview

This project explores how raw conversational data can be processed and used to adapt a Large Language Model (LLM) for a specific domain. It covers the complete workflow, from data generation and preprocessing to model fine-tuning and response evaluation.

## Features

### 1. Data Cleaning & Quality Analysis
- Generated 100 synthetic EMI-related conversation samples with intentionally introduced noise.
- Built a Python-based data cleaning pipeline to filter invalid and inconsistent records.
- Separated cleaned and rejected records for further analysis.
- Generated a quality report to understand data quality and filtering results.

### 2. LLM Fine-Tuning
- Fine-tuned **Qwen2.5-0.5B-Instruct** using LoRA (Low-Rank Adaptation).
- Converted cleaned conversations into an instruction-based training format.
- Trained the model using a Google Colab environment with a T4 GPU.
- Evaluated model responses using simple heuristic-based checks.

### 3. End-to-End Pipeline
The project connects data preprocessing with model training and evaluation to demonstrate a practical workflow for building a domain-specific language model.

**Workflow:**

`Data Generation → Data Cleaning → Quality Analysis → Dataset Preparation → LLM Fine-Tuning → Response Evaluation`

## Tech Stack

- **Language:** Python
- **LLM:** Qwen2.5-0.5B-Instruct
- **Fine-Tuning:** LoRA
- **Libraries:** Hugging Face Transformers, PEFT
- **Environment:** Google Colab, T4 GPU
- **Data Format:** JSONL

## Project Structure

```text
.
├── part_a/
│   ├── clean_data.py
│   └── quality_report.py
├── part_b/
│   └── finetune.ipynb
└── README.md
```

## Getting Started

### Part A: Data Cleaning

Navigate to the data processing directory and run the cleaning pipeline:

```bash
cd part_a
python clean_data.py
python quality_report.py
```

The scripts process the generated conversation data, separate valid and rejected records, and produce a data quality report.

### Part B: Model Fine-Tuning

1. Open `part_b/finetune.ipynb` in Google Colab.
2. Upload the cleaned conversation dataset (`cleaned_conversations.jsonl`).
3. Run the notebook cells to prepare the dataset, fine-tune the model, and evaluate its responses.

## Fine-Tuning Notebook

[Open the Google Colab Notebook](https://colab.research.google.com/drive/1gF0O1fjRQ3Wf10EocmQvAB1Wl-6sG9yv)

## Key Learnings

- Building data preprocessing pipelines for noisy conversational datasets.
- Identifying and filtering invalid training records.
- Preparing instruction-based datasets for LLM fine-tuning.
- Applying parameter-efficient fine-tuning with LoRA.
- Running model training in a GPU-enabled environment.
- Evaluating generated responses using basic heuristics.

## Conclusion

This project demonstrates a practical approach to preparing conversational data and fine-tuning a small language model for a domain-specific use case. It combines data engineering fundamentals with hands-on experience in LLM training and evaluation.
