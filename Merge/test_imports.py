#!/usr/bin/env python3
"""
Test script to verify all imports work correctly.
"""

import os
import sys

# Set up Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add multiple possible paths
sys.path.insert(0, current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, os.path.join(parent_dir, 'Merge'))

print(f"Current directory: {current_dir}")
print(f"Parent directory: {parent_dir}")
print(f"Python path: {sys.path[:3]}...")

# Test imports
try:
    from Blog.agents import BlogAgents
    print("✓ Blog.agents imported successfully")
except ImportError as e:
    print(f"❌ Blog.agents import failed: {e}")

try:
    from whitepaper.main import ResearchConverter
    print("✓ whitepaper.main imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.main import failed: {e}")

try:
    from whitepaper.tools import ResearchTools
    print("✓ whitepaper.tools imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.tools import failed: {e}")

try:
    from whitepaper.agents import ResearchAgents
    print("✓ whitepaper.agents imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.agents import failed: {e}")

try:
    from whitepaper.tasks import ResearchTasks
    print("✓ whitepaper.tasks imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.tasks import failed: {e}")

try:
    from whitepaper.crews import ResearchCrews
    print("✓ whitepaper.crews imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.crews import failed: {e}")

try:
    from whitepaper.exporters import ContentExporters
    print("✓ whitepaper.exporters imported successfully")
except ImportError as e:
    print(f"❌ whitepaper.exporters import failed: {e}")

print("\nTest completed!") 