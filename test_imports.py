#!/usr/bin/env python3
"""Test script to verify all imports work"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing imports...")

try:
    print("✓ Importing path_helper...", end=" ")
    from path_helper import get_data_path
    print("OK")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Testing data paths...", end=" ")
    questions_path = get_data_path("questions.json")
    highscores_path = get_data_path("highscores.json")
    print("OK")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)

try:
    print("✓ Loading JSON data...", end=" ")
    import json
    with open(get_data_path("questions.json"), "r", encoding="utf-8") as f:
        questions = json.load(f)
    print(f"OK ({len(questions['categories'])} categories)")
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)

print("\nAll imports and data files OK!")
