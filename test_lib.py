#!/usr/bin/env python3
"""Пример использования библиотеки gendiff."""

import os

from gendiff import generate_diff


def get_path(*parts):
    """Вспомогательная функция для построения путей."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, *parts)


def main():
    # Плоские файлы
    flat1 = get_path("tests", "test_data", "flat", "file1.json")
    flat2 = get_path("tests", "test_data", "flat", "file2.json")

    print("=== Пример 1: Плоские JSON файлы ===")
    print(generate_diff(flat1, flat2))

    # Вложенные файлы
    nested1 = get_path("tests", "test_data", "nested", "file1.json")
    nested2 = get_path("tests", "test_data", "nested", "file2.json")

    print("\n=== Пример 2: Вложенные JSON файлы ===")
    print(generate_diff(nested1, nested2))

    # Разные форматы
    print("\n=== Пример 3: JSON формат вывода ===")
    print(generate_diff(flat1, flat2, format="json"))


if __name__ == "__main__":
    main()
