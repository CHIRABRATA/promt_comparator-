from runner import run_prompt
from diff_engine import get_diff

def smart_score(output, context, question):
    score = 0
    output_lower = output.lower()

    # 1. Context usage
    for word in context.lower().split():
        if word in output_lower:
            score += 1

    # 2. Length (more detailed = better)
    score += len(output.split()) * 0.05

    # 3. Important keywords (domain logic)
    keywords = ["rain", "soil", "irrigate", "crop"]
    for k in keywords:
        if k in output_lower:
            score += 2

    # 4. Penalize hallucination (basic)
    if "i don't know" in output_lower:
        score -= 2

    return score

def llm_judge(outputs, question, context):
    judge_prompt = f"""
You are an evaluator.

Question: {question}

Context:
{context}

We have these answers:
{outputs}

Return in this format ONLY:

Best: <number>
Reason: <short reason>
Score Breakdown:
- Relevance: x/10
- Context Use: x/10
- Clarity: x/10
"""

    result = run_prompt(judge_prompt, "", "")
    return result

def compare_prompts(prompts, question, context, model="mistral"):
    """
    Runs multiple prompts and compares outputs
    """

    outputs = []

    print("\n🚀 Running Prompt Comparisons...\n")

    # Run all prompts
    for i, prompt in enumerate(prompts):
        print(f"\n==============================")
        print(f"🔹 Prompt {i+1}")
        print(f"==============================")

        output = run_prompt(prompt, question, context, model)
        outputs.append(output)

        print(output)

    # Pairwise diff comparison
    print("\n\n🧠 DIFF COMPARISON:\n")

    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            print(f"\n--- DIFF (P{i+1} vs P{j+1}) ---")
            print(get_diff(outputs[i], outputs[j]))

    # Simple scoring (based on context word usage)
    print("\n\n🏆 SCORING:\n")

    scores = []

    for i, output in enumerate(outputs):
        score = smart_score(output, context, question)
        scores.append(score)

        print(f"Prompt {i+1} Score: {score:.2f}")

    best_index = scores.index(max(scores))

    print(f"\n✅ BEST PROMPT: Prompt {best_index + 1}")

    # LLM Judge evaluation
    print("\n🤖 LLM JUDGE RESULT:\n")
    print(llm_judge(outputs, question, context))

    return outputs