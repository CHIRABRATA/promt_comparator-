import requests

def run_prompt(prompt, question, context, model="mistral"):
    """
    Sends prompt + question + context to local LLM (Ollama)
    """

    full_prompt = f"""
Context:
{context}

Instruction:
{prompt}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": full_prompt,
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "").strip()