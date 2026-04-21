# 🚀 GitHub Actions + PyPI Publishing Setup Guide

## Complete Step-by-Step Instructions

### Your Repository Details
```
GitHub Organization: CHIRABRATA
Repository: promt_comparator-
GitHub URL: https://github.com/CHIRABRATA/promt_comparator-.git
Workflow File: .github/workflows/publish.yml
PyPI Environment: pypi
```

---

## ✅ Step 1: Create PyPI API Token

### 1.1 Go to PyPI.org
- Visit: https://pypi.org
- Sign in (or create account if needed)

### 1.2 Create API Token
1. Click your username → **Account settings**
2. Left sidebar → **API tokens**
3. Click **"Add API token"**
4. Name it: `github-actions-promptdiff`
5. Scope: **Entire account** (or just your project)
6. Click **"Create token"**
7. **Copy the token** (starts with `pypi-`)
   - ⚠️ Save it! You won't see it again!

Example token:
```
pypi-AgEIcHlwaS5vcmc...
```

---

## ✅ Step 2: Add GitHub Secret

### 2.1 Go to GitHub Repository Settings
1. Go to: https://github.com/CHIRABRATA/promt_comparator-/settings
2. Left sidebar → **Secrets and variables** → **Actions**

### 2.2 Create New Repository Secret
1. Click **"New repository secret"**
2. **Name**: `PYPI_API_TOKEN`
3. **Value**: Paste the token from Step 1.2
4. Click **"Add secret"**

✅ Now GitHub can authenticate with PyPI

---

## ✅ Step 3: Create GitHub Environment (Optional but Recommended)

### 3.1 Set Up Environment
1. Go to: https://github.com/CHIRABRATA/promt_comparator-/settings/environments
2. Click **"New environment"**
3. Name: `pypi`
4. Click **"Configure environment"**

### 3.2 Add Deployment Branch
1. Check: **"Require a new review before deploying to this environment"** (optional)
2. Allowed branches: `main` or `*`
3. Click **"Save protection rules"** if needed

### 3.3 Add Environment Secret
1. In the `pypi` environment, scroll to **"Environment secrets"**
2. Click **"Add secret"**
3. **Name**: `PYPI_API_TOKEN`
4. **Value**: Same token from Step 1.2
5. Click **"Add secret"**

---

## ✅ Step 4: Workflow File Location

The workflow file has been created here:
```
.github/workflows/publish.yml
```

### File Structure in Repository
```
promt_comparator-/
├── .github/
│   └── workflows/
│       └── publish.yml          ✅ Already created!
├── promptdiff/
├── pyproject.toml
├── README.md
└── ...
```

---

## ✅ Step 5: How the Workflow Works

### Trigger Events

**Option 1: Tag Push (Recommended)**
```bash
git tag v0.1.0
git push origin v0.1.0
```

Automatically triggers workflow when you push a version tag!

**Option 2: Manual Trigger**
- Go to: https://github.com/CHIRABRATA/promt_comparator-/actions
- Click **"Publish to PyPI"** workflow
- Click **"Run workflow"** button

### Workflow Steps

```
1. Build Job (runs on Ubuntu)
   ├─ Checkout code
   ├─ Setup Python 3.x
   ├─ Install build tools (build, twine)
   ├─ Build distributions (tar.gz + wheel)
   └─ Upload to artifacts
   
2. Publish Job (waits for Build job)
   ├─ Download distributions
   ├─ Authenticate with PyPI
   └─ Upload to PyPI
   
3. Release Job (after successful publish)
   ├─ Create GitHub Release
   └─ Link to CHANGELOG.md
```

---

## 🚀 Publishing Your Package

### Method 1: Using Git Tags (Recommended)

```bash
# 1. Make sure everything is committed
git add .
git commit -m "v0.1.0: Initial release"
git push origin main

# 2. Create version tag
git tag v0.1.0

# 3. Push tag to trigger workflow
git push origin v0.1.0

# 4. Check workflow progress
# Go to: https://github.com/CHIRABRATA/promt_comparator-/actions
```

### Method 2: Manual Trigger (Without Tags)

1. Go to: https://github.com/CHIRABRATA/promt_comparator-/actions
2. Select **"Publish to PyPI"** workflow from left sidebar
3. Click **"Run workflow"** dropdown
4. Click **"Run workflow"** button

---

## 📋 Pre-Publishing Checklist

Before running the workflow:

- [ ] Update version in `promptdiff/__init__.py` to 0.1.0
- [ ] Update version in `pyproject.toml` to 0.1.0
- [ ] Update version in `setup.py` to 0.1.0
- [ ] Update `CHANGELOG.md` with release notes
- [ ] Update author name/email in `pyproject.toml`
- [ ] Commit all changes: `git add . && git commit -m "Prepare v0.1.0"`
- [ ] Push to main: `git push origin main`
- [ ] Test locally: `pip install -e .`
- [ ] Verify examples work: `python examples/example1_basic.py`
- [ ] Create and push tag: `git tag v0.1.0 && git push origin v0.1.0`

---

## 🔍 Monitor Workflow Execution

### Watch Real-Time
1. Go to: https://github.com/CHIRABRATA/promt_comparator-/actions
2. Click the running workflow
3. Watch logs in real-time

### Check Status
- **Green checkmark** ✅ = Success!
- **Red X** ❌ = Failed (check logs)
- **Yellow dot** 🟡 = Running

### View Build Logs
1. Click the job name (e.g., "build")
2. Expand each step to see output
3. Look for errors in **red text**

---

## ✅ After Successful Publish

### 1. Verify on PyPI
```bash
# Check if package is available
pip index versions promptdiff

# Or visit:
# https://pypi.org/project/promptdiff/
```

### 2. Test Installation
```bash
# Install from PyPI (not local)
pip install promptdiff

# Verify it works
python -c "from promptdiff import compare_prompts; print('✅ Works!')"
```

### 3. Check GitHub Release
- Visit: https://github.com/CHIRABRATA/promt_comparator-/releases
- Your release should appear there automatically!

---

## 🐛 Troubleshooting

### Error: "401 Unauthorized"
**Cause:** Wrong or expired PyPI token
**Fix:** 
1. Generate new token on PyPI.org
2. Update secret: https://github.com/CHIRABRATA/promt_comparator-/settings/secrets/actions/PYPI_API_TOKEN

### Error: "Tag already exists"
**Cause:** Tried to push a tag that already exists
**Fix:**
```bash
# Delete local tag
git tag -d v0.1.0

# Delete remote tag
git push origin --delete v0.1.0

# Create new tag
git tag v0.1.0
git push origin v0.1.0
```

### Error: "No module named 'build'"
**Fix:** Workflow will install it automatically, but if using locally:
```bash
pip install build twine
```

### Error: "Version already exists on PyPI"
**Cause:** You already published 0.1.0
**Fix:** Bump version to 0.1.1 or 0.2.0
```bash
# Update version in 3 files
# 1. promptdiff/__init__.py: version = "0.1.1"
# 2. pyproject.toml: version = "0.1.1"
# 3. setup.py: version = "0.1.1"

git add .
git commit -m "Bump version to 0.1.1"
git push
git tag v0.1.1
git push origin v0.1.1
```

### Workflow Not Triggering
**Cause:** Tag format wrong
**Fix:** Use format `v*` or `v0.1.0`
```bash
# Correct ✅
git tag v0.1.0

# Wrong ❌
git tag 0.1.0
git tag version-0.1.0
```

---

## 📊 Workflow Configuration Reference

### Your Configuration

```yaml
Trigger: Push tags matching "v*" (e.g., v0.1.0, v1.0.0)
or: Manual trigger via Actions tab

Jobs:
  1. build - Compiles the package
  2. publish-to-pypi - Publishes to PyPI
  3. github-release - Creates GitHub release

Environment: pypi
Secret: PYPI_API_TOKEN

Python Version: 3.x (latest)
OS: Ubuntu latest
```

### Customization Options

**To trigger on every commit to main:**
```yaml
on:
  push:
    branches: [main]
    tags: ['v*']
```

**To use specific Python version:**
```yaml
python-version: '3.11'  # Instead of '3.x'
```

**To skip GitHub release creation:**
Remove the `github-release` job section

---

## 🔐 Security Best Practices

1. ✅ Use **environment secrets** (not repository secrets)
2. ✅ Regenerate token if compromised
3. ✅ Use **scoped tokens** when possible
4. ✅ Review workflow logs for sensitive data
5. ✅ Never commit `.pypirc` with token
6. ✅ Use **branch protection** on main

---

## 📈 Version Bumping Strategy

### Semantic Versioning
```
MAJOR.MINOR.PATCH
0.1.0

MAJOR: Breaking changes
MINOR: New features (backward compatible)
PATCH: Bug fixes
```

### Example Release Sequence
```
v0.1.0 - Initial release
v0.1.1 - Bug fix
v0.2.0 - New features (AI judge)
v1.0.0 - Major release (stable)
```

---

## 📝 Creating Release Notes

Update `CHANGELOG.md` for each release:

```markdown
## [0.1.0] - 2024-04-21

### Added
- Initial release
- Smart prompt comparison
- LLM-as-judge evaluation

### Fixed
- Removed verbose diff output

### Known Issues
- Requires Ollama running locally
```

---

## 🎯 Next Steps

1. ✅ Generate PyPI API token
2. ✅ Add GitHub secret: `PYPI_API_TOKEN`
3. ✅ (Optional) Create `pypi` environment
4. ✅ Update versions in code
5. ✅ Commit changes
6. ✅ Create tag: `git tag v0.1.0`
7. ✅ Push tag: `git push origin v0.1.0`
8. ✅ Watch workflow in GitHub Actions
9. ✅ Verify on PyPI: https://pypi.org/project/promptdiff/
10. ✅ Test: `pip install promptdiff`

---

## 🔗 Useful Links

- PyPI.org: https://pypi.org
- Your Package: https://pypi.org/project/promptdiff/
- GitHub Actions Docs: https://docs.github.com/en/actions
- Publishing Guide: https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-and-codecov/

---

## 💡 Pro Tips

### Automate Version Bumping
```bash
# Using bump2version
pip install bump2version
bumpversion patch  # Bumps 0.1.0 → 0.1.1
```

### Test Before Publishing
```bash
# Build locally
python -m build

# Check with twine
twine check dist/*

# Test install
pip install dist/promptdiff-0.1.0-py3-none-any.whl
```

### Keep Git History Clean
```bash
git log --oneline
# 5a3f2b Release v0.1.0
# 4e2c1a Add examples
# 3d1b0a Initial commit
```

---

## ✨ Summary

Your GitHub Actions workflow is now configured to:

✅ Build your package automatically
✅ Publish to PyPI with one command
✅ Create GitHub releases automatically
✅ Use secure authentication with API tokens
✅ Support version management

**You're ready to publish! 🚀**

---

Made with 🔥 for the Python packaging community!
