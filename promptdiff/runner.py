import requests

def run_prompt(prompt, question, context, model="mistral", debug=False):
    full_prompt = f"""
Context:
{context}

Instruction:
{prompt}

Question:
{question}

Answer:
"""

    if debug:
        print("\n📤 Sending Prompt:\n", full_prompt)

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": full_prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        return f"❌ Error connecting to model: {e}"

    data = response.json()

    if "response" not in data:
        return "❌ Invalid response from model"

    return data["response"].strip()