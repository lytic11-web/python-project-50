def format_stylish(diff: dict, depth: int = 0) -> str:
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
            lines.append(f"{indent}    - {key}: {old_formatted}")
            lines.append(f"{indent}    + {key}: {new_formatted}")

        elif node_type == "added":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}    + {key}: {formatted_value}")

        elif node_type == "removed":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}    - {key}: {formatted_value}")

        elif node_type == "unchanged":
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{indent}      {key}: {formatted_value}")

    # Для корневого уровня добавляем фигурные скобки
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "\n".join(lines)


def format_value(value, depth: int) -> str:
    """
    Форматирует значение для вывода в stylish формате.

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
        lines.append(f"{indent}" + "}")
        return "\n".join(lines)

    # Специальные преобразования
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    else:
        return str(value)
