# 📁 Project Structure

## Library Structure

```
promptdiff/                    # Main package
├── __init__.py              # Package entry point, exports main functions
├── comparator.py            # Core comparison logic
├── runner.py                # LLM execution (Ollama integration)
└── diff_engine.py          # Diff comparison utilities

pyproject.toml              # Modern Python project config (PyPI)
setup.py                    # Setup script (backward compatibility)
setup.cfg                   # Setup configuration
requirements.txt            # Python dependencies
README.md                   # Main documentation
LICENSE                     # MIT License
MANIFEST.in                 # Files to include in distribution
CONTRIBUTING.md             # Contribution guidelines

examples/                   # Example usage
├── example1_basic.py       # Basic prompt comparison
└── example2_rag.py        # RAG integration example

tests/                      # Test suite
├── __init__.py
├── test_comparator.py
├── test_scoring.py
└── test_integration.py
```

## Usage in Your Project

```
your_project/
│
├── main.py                     # Entry point (user asks question)
├── llm.py                      # LLM integration
├── knowledge_base.py           # RAG pipeline & embeddings
│
├── prompt_testing/             # Using promptdiff 🔥
│   ├── test_prompts.py
│   ├── compare_results.py
│   ├── prompts/
│   │   ├── p1.txt
│   │   ├── p2.txt
│   │   ├── p3.txt
│   │   └── p4.txt
│   │
│   └── context_samples/
│       ├── medical.txt
│       └── technical.txt
│
├── best_prompt.txt             # ✅ Final selected prompt
│
└── requirements.txt
```

## Installation & Setup

### 1. Install from PyPI (Once Published)
```bash
pip install promptdiff
```

### 2. Local Development Install
```bash
git clone https://github.com/CHIRABRATA/promt_comparator-.git
cd promt_comparator-
pip install -e .
```

### 3. Install with Dev Dependencies
```bash
pip install -e .[dev]
```

## Files Explained

### Core Library Files

**`promptdiff/__init__.py`**
- Exports main functions: `compare_prompts`, `llm_advice`
- Defines version and metadata
- Provides package documentation

**`promptdiff/comparator.py`**
- Main comparison logic
- `compare_prompts()` - Compare multiple prompts
- `llm_advice()` - Get AI explanations
- Smart scoring algorithm

**`promptdiff/runner.py`**
- Executes prompts via Ollama
- `run_prompt()` - Calls local LLM
- Handles model parameters

**`promptdiff/diff_engine.py`**
- Generates diff between outputs
- `get_diff()` - Detailed comparison

### Configuration Files

**`pyproject.toml`** (Recommended for modern Python)
```toml
[project]
name = "promptdiff"
version = "0.1.0"
description = "..."
dependencies = ["requests>=2.28.0"]
```

**`setup.py`** (For backward compatibility)
```python
setup(
    name="promptdiff",
    version="0.1.0",
    ...
)
```

**`requirements.txt`**
```
requests>=2.28.0
```

### Documentation Files

**`README.md`**
- Installation instructions
- Quick start guide
- Full API reference
- Use cases and examples
- Troubleshooting

**`CONTRIBUTING.md`**
- Development setup
- Code style guidelines
- Testing instructions
- PR process

**`LICENSE`**
- MIT License
- Legal terms

### Example Files

**`examples/example1_basic.py`**
- Basic usage of promptdiff
- Compare 3 prompts
- Save best result

**`examples/example2_rag.py`**
- RAG integration
- Retrieve context from knowledge base
- Compare with real-world data

## Publishing to PyPI

### Step 1: Install Build Tools
```bash
pip install build twine
```

### Step 2: Build Distribution
```bash
python -m build
```

This creates:
- `dist/promptdiff-0.1.0.tar.gz` (source)
- `dist/promptdiff-0.1.0-py3-none-any.whl` (wheel)

### Step 3: Upload to PyPI

**Test PyPI First:**
```bash
twine upload --repository testpypi dist/*
```

**Production PyPI:**
```bash
twine upload dist/*
```

### Step 4: Verify Installation
```bash
pip install promptdiff
python -c "import promptdiff; print(promptdiff.__version__)"
```

## Project Statistics

- **Python Version**: 3.8+
- **License**: MIT
- **Main Dependencies**: requests
- **Dev Dependencies**: pytest, black, flake8
- **Lines of Code**: ~200 (core)
- **Test Coverage**: Aim for >80%

## Version Bumping

When releasing new versions:

1. Update `__version__` in `promptdiff/__init__.py`
2. Update `version` in `pyproject.toml`
3. Update `version` in `setup.py`
4. Update `CHANGELOG.md` with changes
5. Create git tag: `git tag v0.1.0`
6. Build and upload: `python -m build && twine upload dist/*`

## Common Commands

```bash
# Install locally for development
pip install -e .

# Run tests
pytest

# Format code
black .

# Check linting
flake8 .

# Build distribution
python -m build

# Upload to PyPI
twine upload dist/*

# Check package info
pip show promptdiff
```

## Dependencies Graph

```
promptdiff
  └── runner.py
       └── requests (HTTP calls to Ollama)
  └── comparator.py
       └── runner.py
  └── diff_engine.py
```

## Next Steps

1. ✅ Create PyPI account: https://pypi.org
2. ✅ Generate API token for twine
3. ✅ Update metadata in pyproject.toml
4. ✅ Build package: `python -m build`
5. ✅ Upload: `twine upload dist/*`
6. ✅ Install and test: `pip install promptdiff`

---

**Questions?** See CONTRIBUTING.md or open an issue!
