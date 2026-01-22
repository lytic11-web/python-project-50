#!/usr/bin/env python3
"""Пример использования библиотеки gendiff."""

import os
from gendiff import generate_diff


def main():
    # Пути к тестовым данным
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Вариант 1: Плоские файлы
    flat_file1 = os.path.join(current_dir, "tests", "test_data", "flat", "file1.json")
    flat_file2 = os.path.join(current_dir, "tests", "test_data", "flat", "file2.json")
    
    print("=== Пример 1: Сравнение плоских JSON файлов ===")
    diff = generate_diff(flat_file1, flat_file2)
    print(diff)
    
    # Вариант 2: Вложенные файлы
    nested_file1 = os.path.join(current_dir, "tests", "test_data", "nested", "file1.json")
    nested_file2 = os.path.join(current_dir, "tests", "test_data", "nested", "file2.json")
    
    print("\n=== Пример 2: Сравнение вложенных JSON файлов ===")
    diff_nested = generate_diff(nested_file1, nested_file2)
    print(diff_nested)
    
    # Вариант 3: Разные форматы вывода
    print("\n=== Пример 3: JSON формат вывода ===")
    diff_json = generate_diff(flat_file1, flat_file2, format="json")
    print(diff_json)


if __name__ == "__main__":
    main()
