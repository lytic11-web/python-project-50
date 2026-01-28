#!/usr/bin/env python3
"""Демонстрационный файл для учебного проекта.
Показывает пример использования библиотеки gendiff как
внешнего модуля. Не является частью автоматических тестов.
"""

import os
import sys

# Добавляем корень проекта в Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gendiff import generate_diff


def get_path(*parts):
    """Вспомогательная функция для построения путей от корня проекта."""
    # Просто поднимаемся на один уровень выше от расположения test_lib.py
    return os.path.join(os.path.dirname(__file__), "..", *parts)


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

    # Разные форматы вывода
    print("\n=== Пример 3: JSON формат вывода ===")
    print(generate_diff(flat1, flat2, format="json"))

    print("\n=== Пример 4: Plain формат вывода ===")
    print(generate_diff(nested1, nested2, format="plain"))

    # Пример с YAML файлами
    print("\n=== Пример 5: YAML файлы ===")
    yaml1 = get_path("tests", "test_data", "flat", "file1.yml")
    yaml2 = get_path("tests", "test_data", "flat", "file2.yml")
    print(generate_diff(yaml1, yaml2))

    print("\n=== Пример 6: Вложенные YAML в стиле stylish ===")
    yaml_nested1 = get_path("tests", "test_data", "nested", "file1.yml")
    yaml_nested2 = get_path("tests", "test_data", "nested", "file2.yml")
    print(generate_diff(yaml_nested1, yaml_nested2, format="stylish"))


if __name__ == "__main__":
    main()
