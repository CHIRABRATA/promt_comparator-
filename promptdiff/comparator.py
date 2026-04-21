from runner import run_prompt
from diff_engine import get_diff

def compare_prompts(prompts, question, context, model="mistral"):
    outputs = []

    print("\n🚀 Running Prompt Comparisons...\n")

    # Run prompts
    for i, prompt in enumerate(prompts):
        print(f"\n🔹 Prompt {i+1}")
        output = run_prompt(prompt, question, context, model)
        outputs.append(output)
        print(output)

    # Diff
    print("\n🧠 DIFF:\n")
    for i in range(len(outputs)):
        for j in range(i + 1, len(outputs)):
            print(f"\n--- P{i+1} vs P{j+1} ---")
            print(get_diff(outputs[i], outputs[j]))

    # 🔥 Smart scoring
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

    # 🔥 RETURN IMPORTANT DATA
    return {
        "best_prompt": prompts[best_index],
        "best_index": best_index,
        "outputs": outputs,
        "scores": scores
    }