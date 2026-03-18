# Part B — LLM Finetuning Writeup

## 1. Model Selection

I selected **Qwen2.5-0.5B-Instruct** as the base model because it is lightweight (less than 1B parameters) and suitable for running on Google Colab’s free T4 GPU. It provides a good balance between performance and computational efficiency, making it ideal for this assignment.

---

## 2. LoRA Configuration

I used LoRA (Low-Rank Adaptation) via the PEFT library to efficiently fine-tune the model without updating all parameters.

Configuration used:

* Rank (r): 8
* Alpha: 16
* Target modules: `q_proj`, `v_proj`
* Dropout: 0.05

LoRA was chosen because it reduces memory usage and training time while still allowing the model to adapt to the EMI collection task.

---

## 3. Data Preparation

The cleaned dataset from Part A was converted into an instruction-style format:

* Each sample was structured as:

  * System instruction: "You are a polite EMI collection agent"
  * User message: Customer input
  * Assistant response: Agent reply

This helped guide the model to generate responses in the desired tone and context (Hinglish EMI collection).

---

## 4. Training Setup

* Training was performed using HuggingFace Transformers and Trainer API.
* Batch size: 2
* Epochs: 1
* Dataset size: ~60–70 samples

The goal was to demonstrate a working pipeline rather than achieving high accuracy.

---

## 5. Results and Observations

* The training pipeline ran successfully end-to-end.
* The model was able to generate EMI-related responses after fine-tuning.
* However, due to limited data and training steps, outputs were sometimes inconsistent or generic.

---

## 6. What Went Well

* Successfully implemented LoRA-based fine-tuning on a small model.
* Data pipeline from cleaning to training worked smoothly.
* Model was able to adapt partially to the EMI collection domain.

---

## 7. Challenges Faced

* Handling tokenization and label formatting correctly for training.
* Ensuring compatibility with the latest HuggingFace Trainer API.
* Limited dataset size affected output quality.

---

## 8. Improvements with More Time and Resources

If more time and compute were available, I would:

* Use a larger and more diverse dataset.
* Train for more epochs and tune hyperparameters.
* Use better prompt formatting and instruction tuning.
* Implement more robust evaluation metrics (BLEU, ROUGE, etc.).

---

## 9. Production-Level Improvements (Top 3)

1. Improve dataset quality and scale significantly.
2. Use better evaluation pipelines with human feedback.
3. Fine-tune with larger models and optimized hyperparameters.

---

## 10. Key Takeaway

This task demonstrated how to build a complete fine-tuning pipeline using LoRA, from data preparation to evaluation. Even with limited resources, it is possible to adapt a small LLM to a specific domain effectively.
