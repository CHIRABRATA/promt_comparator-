from comparator import compare_prompts


context = """
Soil: Dry
Rain expected tomorrow
Crop: Rice
"""

question = "Should I irrigate today?"

# Different prompt styles
P1 = "Give farming advice."

P2 = "Use the context and give clear farming advice."

P3 = "Use ONLY the context. If rain is expected, warn the farmer. Give step-by-step advice."

prompts = [P1, P2, P3]

# Run comparison
compare_prompts(prompts, question, context)