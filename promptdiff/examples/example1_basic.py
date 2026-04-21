"""
Example 1: Basic Prompt Comparison

This example shows how to use promptdiff to compare multiple prompts
and find the best one.
"""

from promptdiff import compare_prompts

# Define your prompts
PROMPT_1 = """
You are a medical expert. Answer the following question:
{question}

Provide a comprehensive answer.
"""

PROMPT_2 = """
Answer this medical question concisely:
{question}

Focus on practical information.
"""

PROMPT_3 = """
As a healthcare professional, explain:
{question}

Include symptoms, causes, and treatment options.
"""

# Your question
question = "What are symptoms of diabetes?"

# Context (could come from RAG)
context = """
Diabetes mellitus is a metabolic disorder.
Types: Type 1, Type 2, Gestational
Common symptoms: fatigue, thirst, vision problems
Treatment: insulin, medication, lifestyle changes
"""

# Run comparison
result = compare_prompts(
    prompts=[PROMPT_1, PROMPT_2, PROMPT_3],
    question=question,
    context=context,
    model="mistral"
)

# Access results
print("\n" + "="*50)
print("COMPARISON RESULTS")
print("="*50)

best_index = result["best_index"]
best_score = result["scores"][best_index]

print(f"\n🏆 Best Prompt: P{best_index + 1}")
print(f"📊 Score: {best_score:.2f}")
print(f"\n📝 All Scores: {[f'{s:.2f}' for s in result['scores']]}")

# Save best prompt
with open("best_prompt_example1.txt", "w") as f:
    f.write(result["best_prompt"])

print("\n✅ Best prompt saved to best_prompt_example1.txt")
