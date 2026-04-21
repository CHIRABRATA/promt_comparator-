# 🔥 promptdiff

**Smart prompt comparison & evaluation tool using LLM-as-judge**

Compare multiple prompts side-by-side, get intelligent scoring, AI-powered explanations, and automatically select the best performing prompt.

## ✨ Features

- 🚀 **Run multiple prompts** in parallel with the same question & context
- 🧠 **Smart scoring** - Dynamic keyword matching + length optimization + hallucination detection
- 🤖 **LLM-as-judge** - Get AI-powered explanations for why one prompt wins
- 📊 **Score comparison** - See detailed scores for each prompt (0.00 format)
- 💡 **2-line wisdom** - Concise AI-generated bullet points explaining the best choice
- 🔄 **RAG integration** - Works seamlessly with RAG pipelines and context retrieval

## 📦 Installation

```bash
pip install promptdiff
```

Or from source:
```bash
git clone https://github.com/yourusername/promptdiff.git
cd promptdiff
pip install -e .
```

## 🚀 Quick Start

### Basic Usage

```python
from promptdiff import compare_prompts

# Your prompts
P1 = "What are symptoms of diabetes?"
P2 = "Explain the clinical signs of diabetes mellitus."
P3 = "List all indicators of diabetes disease."

# Question & context
question = "What are symptoms of diabetes?"
context = "diabetes mellitus type 2 symptoms include fatigue, thirst, vision problems"

# Compare!
result = compare_prompts(
    prompts=[P1, P2, P3],
    question=question,
    context=context,
    model="mistral"  # Uses Ollama by default
)

print(result["best_prompt"])
print(f"Score: {result['scores'][result['best_index']]:.2f}")
```

### With RAG (Knowledge Retrieval)

```python
from promptdiff import compare_prompts
from knowledge_base import retrieve_context

# Load your prompts
P1 = open("prompts/p1.txt").read()
P2 = open("prompts/p2.txt").read()
P3 = open("prompts/p3.txt").read()

question = "What are symptoms of diabetes?"

# 🔥 Get real context from your knowledge base (RAG)
context = retrieve_context(question)

# Compare with real context
result = compare_prompts(
    prompts=[P1, P2, P3],
    question=question,
    context=context,
    model="mistral"
)

best_prompt = result["best_prompt"]

# Save the best prompt
with open("../best_prompt.txt", "w") as f:
    f.write(best_prompt)

print("\n✅ BEST PROMPT SAVED")
```

### Output Example

```
🚀 Running Prompt Comparisons...

🔹 Prompt 1
[... model output ...]

🔹 Prompt 2
[... model output ...]

🔹 Prompt 3
[... model output ...]

🏆 SCORING:

Prompt 1: 8.45
Prompt 2: 12.30
Prompt 3: 10.15

✅ BEST PROMPT: P2

💡 WHY THIS IS BEST:

1. Uses clinical terminology effectively and covers complications
2. Provides systematic approach to symptom recognition
```

## 📁 Project Structure

```
project/
│
├── main.py                    # Entry point
├── llm.py                     # LLM integration
├── knowledge_base.py          # RAG pipeline
│
├── prompt_testing/            # Using promptdiff
│   ├── test_prompts.py
│   ├── prompts/
│   │   ├── p1.txt
│   │   ├── p2.txt
│   │   └── p3.txt
│   └── context_sample.txt
│
├── best_prompt.txt            # ✅ Final selected prompt
│
└── pyproject.toml
```

## 🔧 API Reference

### `compare_prompts(prompts, question, context, model="mistral")`

Compares multiple prompts and returns the best one.

**Parameters:**
- `prompts` (list): List of prompt strings to compare
- `question` (str): The question/task to evaluate
- `context` (str): Relevant context (knowledge base, examples, etc.)
- `model` (str): LLM model name (default: "mistral"). Must be available via Ollama

**Returns:** 
Dictionary with:
- `best_prompt`: The winning prompt text
- `best_index`: Index of the best prompt
- `outputs`: All model outputs
- `scores`: Score for each prompt

**Example:**
```python
result = compare_prompts(
    prompts=["Prompt 1", "Prompt 2"],
    question="What is AI?",
    context="Artificial Intelligence is...",
    model="mistral"
)

print(result["best_prompt"])      # Best prompt text
print(result["best_index"])       # 0 or 1
print(result["scores"])           # [8.5, 12.3]
print(result["outputs"])          # Model outputs
```

## 🤖 Scoring System

Scores are calculated using:

1. **Dynamic Keyword Matching** (+1.5 per keyword)
   - Extracts words >3 chars from question + context
   - Rewards outputs that use relevant vocabulary

2. **Length Bonus** (+0.03 per word)
   - Longer, more detailed responses score higher
   - Helps avoid too-brief answers

3. **Length Penalty** (-3 if > 120 words)
   - Prevents overly verbose outputs
   - Balances detail with conciseness

**Example Scores:**
- Incomplete answer: 3.2
- Good answer: 8.5
- Excellent answer: 12.3

## 🐳 Requirements

### Local LLM via Ollama

```bash
# Install Ollama from https://ollama.ai
ollama pull mistral
ollama serve
```

Or use any model available in Ollama:
```bash
ollama pull neural-chat
ollama pull openchat
```

### Python Dependencies

- Python 3.8+
- requests (for API calls)

## 💡 Use Cases

### 1. Prompt Optimization
Find the best-performing prompt for your specific use case

### 2. A/B Testing
Compare different prompt formulations scientifically

### 3. RAG Evaluation
Test which prompt works best with your knowledge base

### 4. Template Selection
Choose between multiple prompt templates

### 5. Fine-tuning Feedback
Get AI-powered insights on why certain prompts work better

## 🔥 Advanced Tips

### Combine with RAG
```python
from knowledge_base import retrieve_context, chunk_documents

# Index your knowledge base
docs = load_documents("docs/")
chunks = chunk_documents(docs)
build_embeddings(chunks)

# Retrieve relevant context
context = retrieve_context(question, top_k=5)

# Compare prompts with real context
result = compare_prompts(prompts, question, context)
```

### Batch Testing
```python
prompts_v1 = [p1, p2, p3]
prompts_v2 = [p4, p5, p6]

result_v1 = compare_prompts(prompts_v1, question, context)
result_v2 = compare_prompts(prompts_v2, question, context)

if result_v2["scores"][result_v2["best_index"]] > \
   result_v1["scores"][result_v1["best_index"]]:
    print("V2 is better!")
```

### Custom Scoring
Extend the scoring logic for your domain:
```python
def custom_score(output, context, question):
    # Your scoring logic here
    pass
```

## 📝 Configuration

### Model Selection
```python
# Use different models
compare_prompts(prompts, question, context, model="neural-chat")
compare_prompts(prompts, question, context, model="openchat")
compare_prompts(prompts, question, context, model="llama2")
```

### Custom Context
```python
# Use external knowledge base
context = """
- Diabetes symptoms: fatigue, thirst
- Types: Type 1, Type 2, Gestational
- Treatment: Insulin, medication, lifestyle
"""

compare_prompts(prompts, question, context)
```

## 🐛 Troubleshooting

### "Connection refused" error
Make sure Ollama is running:
```bash
ollama serve
```

### Model not found
Pull the model first:
```bash
ollama pull mistral
```

### Slow comparisons
- Use a smaller model: `ollama pull neural-chat`
- Run Ollama on GPU for faster inference

## 🤝 Contributing

Contributions welcome! 

```bash
git clone https://github.com/yourusername/promptdiff.git
cd promptdiff
pip install -e .[dev]
pytest
```

## 📄 License

MIT License - see LICENSE file

## 🙏 Credits

Built for prompt engineers, LLM researchers, and RAG practitioners.

## 📧 Support

- Issues: https://github.com/yourusername/promptdiff/issues
- Discussions: https://github.com/yourusername/promptdiff/discussions

---

**Made with 🔥 for the prompt engineering community**
