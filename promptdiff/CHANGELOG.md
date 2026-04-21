# Changelog

All notable changes to the promptdiff project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Web UI dashboard for prompt comparison
- CLI tool for batch testing
- Custom scoring function support
- Prompt history and caching
- API server (FastAPI)
- Docker containerization
- Database backend for results

## [0.1.0] - 2024-04-21

### Added
- ✨ Initial release of promptdiff
- 🚀 `compare_prompts()` - Main comparison function
- 💡 `llm_advice()` - AI-powered explanation generation
- 🧠 Smart scoring algorithm with:
  - Dynamic keyword matching
  - Length optimization
  - Hallucination detection
- 🤖 LLM-as-judge evaluation
- 📊 Detailed scoring metrics
- 🔄 RAG integration ready
- 📚 Comprehensive documentation
  - Full README with examples
  - QUICKSTART guide
  - PROJECT_STRUCTURE guide
  - API reference
- 🔧 Multiple examples:
  - Basic prompt comparison
  - RAG-enhanced comparison
- 🛠️ Development tools:
  - pytest configuration
  - black formatting
  - flake8 linting
- 📦 PyPI publication ready:
  - pyproject.toml
  - setup.py
  - MANIFEST.in
- 📄 Supporting files:
  - MIT License
  - CONTRIBUTING guidelines
  - .gitignore
  - requirements.txt

### Features
- Multi-prompt comparison with single function call
- Automatic best prompt selection
- AI-generated reasoning for choices
- Integration with Ollama for local LLM inference
- Support for multiple models (mistral, neural-chat, openchat, etc.)
- Return structured results with scores and outputs
- Context-aware scoring

### Technical Details
- Pure Python implementation
- Minimal dependencies (requests only)
- Python 3.8+ support
- No external API calls required (local inference via Ollama)
- Lightweight and fast

### Documentation
- 2000+ words of comprehensive documentation
- Usage examples for common scenarios
- RAG integration guide
- Troubleshooting section
- API reference
- Project structure guide

### Known Limitations
- Requires Ollama running locally
- Scoring is keyword-based (not ML-based)
- No persistent storage of comparison history
- Single-turn comparison (no multi-turn dialogs)

### Future Improvements
- ML-based scoring model
- Web UI for easier usage
- API server for remote inference
- Batch processing CLI
- Prompt templates library
- Integration with cloud LLM providers
- Advanced metrics (BLEU, ROUGE)
- A/B testing statistics

---

## Release Notes

### Installation

```bash
pip install promptdiff
```

### Quick Start

```python
from promptdiff import compare_prompts

result = compare_prompts(
    prompts=["prompt1", "prompt2", "prompt3"],
    question="Your question here",
    context="Context from your knowledge base",
    model="mistral"
)

print(f"Best: Prompt {result['best_index'] + 1}")
```

### Requirements

- Python 3.8 or higher
- Ollama installed and running
- Local LLM model (mistral by default)

### Compatibility

Tested with:
- Python 3.8, 3.9, 3.10, 3.11
- Ollama 0.1.0+
- Models: mistral, neural-chat, openchat, llama2

### Support

- GitHub Issues: Report bugs
- GitHub Discussions: Ask questions
- Documentation: See README.md and QUICKSTART.md

### Contributors

- Initial release team

### License

MIT License - See LICENSE file

---

## Migration Guide

### From Previous Versions

If you were using the development version:

**Before:**
```python
from comparator import compare_prompts
result = compare_prompts(...)
```

**After:**
```python
from promptdiff import compare_prompts
result = compare_prompts(...)
```

### API Changes

No breaking changes in v0.1.0 (first release).

---

## Version History

| Version | Release Date | Status | Notes |
|---------|-------------|--------|-------|
| 0.1.0   | 2024-04-21  | Current | Initial release |
| Planned | TBD         | - | Web UI, API server |

---

## Deprecated

None in current version.

---

## Security

For security issues, please email security@example.com instead of using the issue tracker.

---

## Acknowledgments

Built with passion for the prompt engineering community! 🚀

---

For detailed information, see:
- README.md - Full documentation
- QUICKSTART.md - Get started guide
- PROJECT_STRUCTURE.md - Project organization
- CONTRIBUTING.md - How to contribute
