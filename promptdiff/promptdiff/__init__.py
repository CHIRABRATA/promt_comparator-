"""
promptdiff - Smart Prompt Comparison & Evaluation Tool

Compare multiple prompts side-by-side with intelligent LLM-based evaluation.
Get scoring, AI-powered explanations, and automatically select the best prompt.
"""

from .comparator import compare_prompts, llm_advice

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

__all__ = [
    "compare_prompts",
    "llm_advice",
]

# Quick start guide
__doc__ = """
🔥 promptdiff - Smart Prompt Comparison Tool

Quick Start:
    from promptdiff import compare_prompts
    
    result = compare_prompts(
        prompts=["prompt1", "prompt2", "prompt3"],
        question="Your question here",
        context="Relevant context from RAG or knowledge base",
        model="mistral"
    )
    
    print(result["best_prompt"])

Features:
    ✅ Compare multiple prompts at once
    ✅ Smart scoring with keyword matching
    ✅ LLM-as-judge for evaluation
    ✅ AI-generated explanations
    ✅ RAG integration ready

Documentation:
    https://github.com/yourusername/promptdiff

GitHub:
    https://github.com/yourusername/promptdiff
"""
