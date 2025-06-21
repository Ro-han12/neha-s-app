#!/usr/bin/env python3
"""
Deployment script for Streamlit Cloud.
This script sets up the environment and tests all components.
"""

import os
import sys
import subprocess
from pathlib import Path

def install_dependencies():
    """Install required dependencies."""
    print("Installing dependencies...")
    
    # Install from requirements-streamlit.txt
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements-streamlit.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def test_environment():
    """Test the environment setup."""
    print("\nTesting environment...")
    
    # Test basic imports
    try:
        import streamlit
        print("✓ Streamlit imported")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        import crewai
        print("✓ CrewAI imported")
    except ImportError as e:
        print(f"❌ CrewAI import failed: {e}")
        return False
    
    try:
        import duckdb
        print("✓ DuckDB imported")
    except ImportError as e:
        print(f"❌ DuckDB import failed: {e}")
        return False
    
    try:
        import chromadb
        print("✓ ChromaDB imported")
    except ImportError as e:
        print(f"❌ ChromaDB import failed: {e}")
        return False
    
    return True

def test_app_imports():
    """Test app-specific imports."""
    print("\nTesting app imports...")
    
    # Add current directory to path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        from Blog.agents import BlogAgents
        print("✓ Blog.agents imported")
    except ImportError as e:
        print(f"❌ Blog.agents import failed: {e}")
        return False
    
    try:
        from whitepaper.main import ResearchConverter
        print("✓ whitepaper.main imported")
    except ImportError as e:
        print(f"❌ whitepaper.main import failed: {e}")
        return False
    
    return True

def main():
    """Main deployment setup function."""
    print("🚀 Streamlit Cloud Deployment Setup")
    print("=" * 40)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        return 1
    
    # Test environment
    if not test_environment():
        print("❌ Environment test failed")
        return 1
    
    # Test app imports
    if not test_app_imports():
        print("❌ App import test failed")
        return 1
    
    print("\n✅ All tests passed! Ready for deployment.")
    print("\n📋 Deployment Checklist:")
    print("1. Push code to GitHub")
    print("2. Go to share.streamlit.io")
    print("3. Connect your repository")
    print("4. Set path to: Merge/app.py")
    print("5. Use requirements file: requirements-streamlit.txt")
    print("6. Add environment variables:")
    print("   - GOOGLE_API_KEY=your_key_here")
    print("   - CHROMA_DB_IMPL=duckdb")
    print("   - ANONYMIZED_TELEMETRY=False")
    print("   - CHROMA_TELEMETRY_ENABLED=False")
    
    return 0

if __name__ == "__main__":
    exit(main()) 