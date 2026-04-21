"""
Example 2: RAG Integration

This example demonstrates how to use promptdiff with a knowledge base
(RAG - Retrieval-Augmented Generation) to compare prompts with
real-world context.
"""

from promptdiff import compare_prompts

# Simulate retrieving context from your knowledge base
def retrieve_context(question):
    """
    In a real scenario, this would:
    1. Convert question to embedding
    2. Search your vector database
    3. Return top-k relevant documents
    """
    knowledge_base = {
        "diabetes": """
        Diabetes Type 2:
        - Most common form (90% of cases)
        - Usually develops in adults
        - Often preventable with lifestyle changes
        
        Symptoms:
        - Increased thirst and frequent urination
        - Fatigue and weakness
        - Blurred vision
        - Slow healing of cuts/sores
        - Numbness/tingling in hands/feet
        
        Risk Factors:
        - Obesity
        - Family history
        - Age (45+)
        - Physical inactivity
        
        Prevention:
        - Regular exercise (150 min/week)
        - Healthy diet (low sugar)
        - Weight management
        - Regular checkups
        """,
        "treatment": """
        Diabetes Management:
        - Blood sugar monitoring
        - Medications: Metformin, GLP-1 agonists
        - Insulin therapy (if needed)
        - Lifestyle modifications
        - Regular follow-ups with endocrinologist
        """
    }
    
    # Simple keyword matching (in real RAG, use embeddings)
    if "symptom" in question.lower():
        return knowledge_base["diabetes"]
    return knowledge_base["diabetes"] + "\n" + knowledge_base["treatment"]


# Load your prompts (could be from files)
PROMPTS = [
    """You are a diabetes specialist.
    Question: {question}
    Provide accurate, evidence-based information.""",
    
    """As a healthcare professional, explain:
    {question}
    Use simple language for patient understanding.""",
    
    """Medical expert mode:
    {question}
    Include pathophysiology and clinical implications."""
]

# Question to compare
question = "What are the main symptoms of diabetes?"

# Get real context from knowledge base
context = retrieve_context(question)

print(f"📚 Context retrieved from knowledge base ({len(context)} chars)")
print("-" * 50)

# Compare prompts with RAG context
result = compare_prompts(
    prompts=PROMPTS,
    question=question,
    context=context,
    model="mistral"
)

# Display results
print("\n" + "="*50)
print("RAG-ENHANCED COMPARISON")
print("="*50)

best_index = result["best_index"]
print(f"\n🏆 Best Prompt: P{best_index + 1}")
print(f"📊 Scores: {[f'{s:.2f}' for s in result['scores']]}")

# Save best prompt for production use
with open("best_prompt_rag.txt", "w") as f:
    f.write(result["best_prompt"])

print("\n✅ Best prompt with RAG context saved")
