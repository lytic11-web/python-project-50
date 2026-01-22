import json
from typing import Any, Dict

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


def format_stylish(diff: Dict, depth: int = 0) -> str:
    """
    Форматирует дерево различий в stylish формате.

    Args:
        diff: дерево различий
        depth: текущая глубина для отступов

    Returns:
        Строка в формате stylish
    """
    lines = []
    indent = "    " * depth  # 4 пробела на уровень

    for key, node in sorted(diff.items()):
        node_type = node["type"]

        if node_type == "nested":
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node["children"], depth + 1))
            lines.append(f"{indent}    }}")

        elif node_type == "changed":
            old_formatted = format_value(node["old_value"], depth + 1)
            new_formatted = format_value(node["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_formatted}")
            lines.append(f"{indent}  + {key}: {new_formatted}")

        elif node_type == "added":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  + {key}: {formatted_value}")

        elif node_type == "removed":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}  - {key}: {formatted_value}")

        elif node_type == "unchanged":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}    {key}: {formatted_value}")

    # Для корневого уровня добавляем фигурные скобки
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "\n".join(lines)


def format_value(value: Any, depth: int) -> str:
    """
    Форматирует значение для вывода.

    Args:
        value: значение для форматирования
        depth: текущая глубина для отступов

    Returns:
        Отформатированная строка
    """
    if isinstance(value, dict):
        indent = "    " * depth
        lines = ["{"]
        for key, val in sorted(value.items()):
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_val}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)

    # Специальные преобразования
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)


def generate_diff(
    file1_path: str, file2_path: str, format: str = "stylish"
) -> str:
    """
    Основная функция сравнения файлов.

    Args:
        file1_path: путь к первому файлу
        file2_path: путь ко второму файлу
        format: формат вывода

    Returns:
        Строка с различиями в указанном формате
    """
    # Читаем файлы
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)

    # Строим дерево различий
    diff_tree = build_tree(data1, data2)

    # Форматируем вывод
    if format == "stylish":
        return format_stylish(diff_tree)
    elif format == "plain":
        return "Plain format will be implemented later"
    elif format == "json":
        return json.dumps(diff_tree, indent=2)
    else:
        raise ValueError(f"Unsupported format: {format}")


def read_file(file_path: str) -> Dict[str, Any]:
    """Читает и парсит JSON или YAML файлы."""
    return parse_file(file_path)
