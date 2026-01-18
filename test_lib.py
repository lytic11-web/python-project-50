#!/usr/bin/env python3
from gendiff import generate_diff

# Используем как библиотеку
diff = generate_diff("file1.json", "file2.json")
print("Using as library:")
print(diff)

# С другим форматом
diff_json = generate_diff("file1.json", "file2.json", format="json")
print("\nJSON format:")
print(diff_json)
