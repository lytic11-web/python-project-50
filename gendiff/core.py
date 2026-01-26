from typing import Dict

from gendiff.formatters import get_formatter
from gendiff.parsers import parse_file


def build_tree(data1: Dict, data2: Dict) -> Dict:
    """
    Строит дерево различий между двумя словарями.

    Возвращает словарь, где:
    - type: 'unchanged', 'changed', 'added', 'removed', 'nested'
    - value: значение (для unchanged, added, removed)
    - old_value, new_value: для changed
    - children: для nested
    """
    result = {}

    # Все уникальные ключи
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        # Ключ только в первом файле
        if key not in data2:
            result[key] = {"type": "removed", "value": data1[key]}

        # Ключ только во втором файле
        elif key not in data1:
            result[key] = {"type": "added", "value": data2[key]}

        # Ключ в обоих файлах
        else:
            value1 = data1[key]
            value2 = data2[key]

            # Если оба значения - словари, рекурсивно сравниваем
            if isinstance(value1, dict) and isinstance(value2, dict):
                result[key] = {
                    "type": "nested",
                    "children": build_tree(value1, value2),
                }

            # Если значения разные
            elif value1 != value2:
                result[key] = {
                    "type": "changed",
                    "old_value": value1,
                    "new_value": value2,
                }

            # Если значения одинаковые
            else:
                result[key] = {"type": "unchanged", "value": value1}

    return result


def generate_diff(
    file1_path: str, file2_path: str, format: str = "stylish"
) -> str:
    """
    Основная функция сравнения файлов.

    Args:
        file1_path: путь к первому файлу
        file2_path: путь ко второму файлу
        format: формат вывода ('stylish', 'plain', 'json')

    Returns:
        Строка с различиями в указанном формате
    """
    # Читаем файлы
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    # Строим дерево различий
    diff_tree = build_tree(data1, data2)

    formatter = get_formatter(format)
    return formatter(diff_tree)
