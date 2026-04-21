from runner import run_prompt
from diff_engine import get_diff

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
    context_words = context.lower().split()

    for i, output in enumerate(outputs):
        score = sum(1 for word in context_words if word in output.lower())
        scores.append(score)

        print(f"Prompt {i+1} Score: {score}")

    best_index = scores.index(max(scores))

    print(f"\n✅ BEST PROMPT: Prompt {best_index + 1}")

    return outputs