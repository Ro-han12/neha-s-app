#!/usr/bin/env python3
"""
Test script to verify ChromaDB works correctly with simplified configuration.
"""

import os
import sys

# Set ChromaDB environment variables
os.environ["CHROMA_DB_IMPL"] = "duckdb"
os.environ["ANONYMIZED_TELEMETRY"] = "False"
os.environ["CHROMA_TELEMETRY_ENABLED"] = "False"

# Test ChromaDB import
try:
    import chromadb
    print("✓ ChromaDB imported successfully")
    
    # Test ChromaDB client creation with new syntax (no Settings needed)
    client = chromadb.Client()
    print("✓ ChromaDB client created successfully with new syntax")
    
    # Test collection creation
    collection = client.create_collection("test_collection")
    print("✓ ChromaDB collection created successfully")
    
    print("All ChromaDB tests passed!")
    
except Exception as e:
    print(f"❌ ChromaDB test failed: {e}")
    print("This is expected if SQLite version is incompatible")

# Test DuckDB
try:
    import duckdb
    print("✓ DuckDB imported successfully")
    
    # Test DuckDB connection
    conn = duckdb.connect(':memory:')
    print("✓ DuckDB connection created successfully")
    
    # Test simple query
    result = conn.execute("SELECT 1 as test").fetchall()
    print(f"✓ DuckDB query executed: {result}")
    
    print("All DuckDB tests passed!")
    
except Exception as e:
    print(f"❌ DuckDB test failed: {e}")

print("\nTest completed!") 