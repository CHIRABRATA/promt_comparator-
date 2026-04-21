# Contributing to promptdiff

We love your input! We want to make contributing to promptdiff as easy and transparent as possible.

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/promptdiff.git
   cd promptdiff
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e .[dev]
   ```

4. **Run tests**
   ```bash
   pytest
   ```

## Code Style

- Use **Black** for formatting: `black .`
- Use **flake8** for linting: `flake8 .`
- Follow **PEP 8** conventions

## Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and test**
   ```bash
   pytest tests/
   black .
   ```

3. **Commit with clear messages**
   ```bash
   git commit -m "Add: description of your change"
   ```

4. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Types of Contributions

### 🐛 Bug Reports
Include:
- Python version
- OS
- Error message and traceback
- Minimal code to reproduce

### 💡 Feature Requests
Describe:
- Use case
- Expected behavior
- Examples if possible

### 📚 Documentation
- Improve README
- Add examples
- Fix typos
- Clarify complex sections

### 🔧 Code Improvements
- Optimize performance
- Add tests
- Refactor unclear code
- Improve error handling

## Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_comparator.py

# Run with coverage
pytest --cov=promptdiff
```

## Documentation

Keep docstrings updated:
```python
def my_function(param1, param2):
    """
    Short description.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description
        
    Example:
        >>> my_function("a", "b")
        "result"
    """
```

## Commit Messages

Use conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `test:` Tests
- `refactor:` Code reorganization
- `perf:` Performance improvement

Example: `feat: add custom scoring function`

## Pull Request Process

1. Update README if needed
2. Add tests for new features
3. Update CHANGELOG.md
4. Ensure all tests pass
5. Get review from maintainers

## Questions?

Feel free to open an issue or join our discussions!

---

Thank you for contributing! 🚀
