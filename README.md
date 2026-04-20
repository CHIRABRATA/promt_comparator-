 # promt_comparator

**A PyPI-installable tool to compare prompts in RAG systems and identify the most efficient one.**

---

## 💡 Project Idea

When building **RAG (Retrieval-Augmented Generation)** systems, one of the most common challenges is choosing the right prompt. Different prompts can produce very different outputs in terms of quality, accuracy, and efficiency — but it's not always obvious which prompt works best for a given use case or audience.

`promt_comparator` solves this problem by allowing you to **compare up to 3 prompts side-by-side** and automatically **identify which prompt is the most efficient** for your specific RAG pipeline.

---

## 🚀 Features

- 📦 **Easy installation** via `pip` from [PyPI](https://pypi.org/)
- 🔍 **Compare 3 prompts** simultaneously against the same input/context
- 🏆 **Identifies the most efficient prompt** based on response quality metrics
- 🛠️ Designed specifically for use in **RAG (Retrieval-Augmented Generation)** workflows

---

## 📦 Installation

```bash
pip install promt-comparator
```

---

## 🧪 Usage

```python
from promt_comparator import compare_prompts

prompt_1 = "Summarize the following document in 3 bullet points: {context}"
prompt_2 = "Given the context below, provide a concise summary: {context}"
prompt_3 = "You are an expert analyst. Read the context and give a brief summary: {context}"

results = compare_prompts(
    prompts=[prompt_1, prompt_2, prompt_3],
    context="<your document or retrieval context here>"
)

print(results.best_prompt)      # The most efficient prompt
print(results.scores)           # Scores for all 3 prompts
print(results.comparison_table) # Full side-by-side comparison
```

---

## 🎯 Why promt_comparator?

In RAG systems, the prompt acts as the bridge between retrieved context and the language model. A poorly chosen prompt can lead to:

- Incomplete or inaccurate answers
- Higher token usage and cost
- Inconsistent responses across users

`promt_comparator` takes the guesswork out of prompt selection by giving you **data-driven insight** into which prompt performs best — so you can ship better RAG applications faster.

---

## 📋 How It Works

1. You provide **3 candidate prompts** and a **context** (retrieved document/passage).
2. The tool runs each prompt through the configured LLM.
3. Responses are evaluated using configurable metrics (e.g., relevance, conciseness, faithfulness).
4. A **ranking and recommendation** is returned, highlighting the most efficient prompt.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

MIT License
