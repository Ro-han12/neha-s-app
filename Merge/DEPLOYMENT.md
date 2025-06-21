# Deployment Guide

## Module Import Issues Resolution

If you're getting "no module" errors when deploying, follow these steps:

### 1. Check Package Structure
Ensure your directory structure looks like this:
```
Merge/
├── __init__.py          # ✅ Added
├── app.py
├── deploy_helper.py     # ✅ Added
├── requirements.txt
├── Blog/
│   ├── __init__.py      # ✅ Updated
│   ├── agents.py
│   └── ...
└── whitepaper/
    ├── __init__.py      # ✅ Updated
    ├── main.py
    ├── agents.py
    └── ...
```

### 2. Test Local Environment
Run the deployment helper to test your environment:
```bash
cd Merge
python deploy_helper.py
```

### 3. Common Deployment Platforms

#### Streamlit Cloud
- Make sure `app.py` is in the root directory
- Set environment variables in Streamlit Cloud dashboard
- The updated imports should work automatically

#### Heroku
- Add `runtime.txt` with Python version
- Ensure `requirements.txt` is in the root
- The module path setup should handle imports

#### Docker
- Use the provided `Dockerfile` (if available)
- Mount the entire project directory

### 4. Environment Variables
Make sure these are set in your deployment environment:
```bash
GOOGLE_API_KEY=your_api_key_here
CHROMA_DB_IMPL=duckdb
```

### 5. Troubleshooting

#### If imports still fail:
1. Check if all `__init__.py` files exist
2. Verify Python path setup in `app.py`
3. Try running `python -c "import sys; print(sys.path)"` to debug paths
4. Use absolute imports instead of relative imports

#### For specific platforms:
- **Streamlit Cloud**: The updated code should work out of the box
- **Heroku**: May need to add buildpacks for additional dependencies
- **Docker**: Ensure the working directory is set correctly

### 6. Quick Fix
If you're still having issues, you can temporarily inline the imports by copying the required classes directly into `app.py`. However, this is not recommended for maintainability.

## File Changes Made

1. ✅ Added `__init__.py` to Merge directory
2. ✅ Updated `Blog/__init__.py` with proper exports
3. ✅ Updated `whitepaper/__init__.py` with proper exports
4. ✅ Fixed circular imports in `whitepaper/main.py`
5. ✅ Added deployment helper script
6. ✅ Enhanced import error handling in `app.py`
7. ✅ Added Python path setup for deployment environments

These changes should resolve the "no module" errors you're experiencing during deployment. 