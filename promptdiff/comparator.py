from runner import run_prompt
from diff_engine import get_diff

def llm_advice(best_output, question, context):
    """Get 2-line pointwise explanation from LLM"""
    judge_prompt = f"""Question: {question}

Context: {context}

Best Answer:
{best_output}

Provide 2 bullet points why this is the best:
1. 
2. 

Keep it concise, practical."""

    result = run_prompt(judge_prompt, "", "")
    return result

def compare_prompts(prompts, question, context, model="mistral"):
    outputs = []

    print("\n🚀 Running Prompt Comparisons...\n")

    
    for i, prompt in enumerate(prompts):
        print(f"\n🔹 Prompt {i+1}")
        output = run_prompt(prompt, question, context, model)
        outputs.append(output)
        print(output)


    def smart_score(output):
        score = 0
        output_lower = output.lower()

        # dynamic keywords
        words = (context + " " + question).lower().split()
        keywords = list(set([w for w in words if len(w) > 3]))

        for k in keywords:
            if k in output_lower:
                score += 1.5

        # length control
        length = len(output.split())
        score += length * 0.03

        if length > 120:
            score -= 3

        return score

    scores = []
    print("\n🏆 SCORING:\n")

    for i, out in enumerate(outputs):
        s = smart_score(out)
        scores.append(s)
        print(f"Prompt {i+1}: {s:.2f}")

    best_index = scores.index(max(scores))

    print(f"\n✅ BEST PROMPT: P{best_index+1}")

    # 🤖 LLM ADVICE
    print("\n💡 WHY THIS IS BEST:\n")
    advice = llm_advice(outputs[best_index], question, context)
    print(advice)

    # 🔥 RETURN IMPORTANT DATA
    return {
        "best_prompt": prompts[best_index],
        "best_index": best_index,
        "outputs": outputs,
        "scores": scores
    }