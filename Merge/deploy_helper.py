#!/usr/bin/env python3
"""
Deployment helper script to resolve module import issues.
This script helps ensure all required modules are properly importable.
"""

import os
import sys
from pathlib import Path

def setup_python_path():
    """Setup Python path to include all necessary directories."""
    # Get the current directory
    current_dir = Path(__file__).parent.absolute()
    
    # Add current directory to Python path
    if str(current_dir) not in sys.path:
        sys.path.insert(0, str(current_dir))
    
    # Add parent directory to Python path
    parent_dir = current_dir.parent
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))
    
    print(f"Python path setup complete:")
    print(f"Current directory: {current_dir}")
    print(f"Parent directory: {parent_dir}")
    print(f"Python path: {sys.path[:3]}...")

def test_imports():
    """Test if all required modules can be imported."""
    try:
        print("Testing imports...")
        
        # Test Blog imports
        from Blog.agents import BlogAgents
        print("✓ Blog.agents imported successfully")
        
        # Test whitepaper imports
        from whitepaper.main import ResearchConverter
        from whitepaper.tools import ResearchTools
        from whitepaper.agents import ResearchAgents
        from whitepaper.tasks import ResearchTasks
        from whitepaper.crews import ResearchCrews
        from whitepaper.exporters import ContentExporters
        print("✓ All whitepaper modules imported successfully")
        
        print("All imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    """Main function to setup and test the environment."""
    print("Setting up deployment environment...")
    
    # Setup Python path
    setup_python_path()
    
    # Test imports
    if test_imports():
        print("Environment setup successful!")
        return 0
    else:
        print("Environment setup failed!")
        return 1

if __name__ == "__main__":
    exit(main()) 