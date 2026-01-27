def format_stylish(diff: dict, depth: int = 0) -> str:
    """
    Форматирует дерево различий в stylish формате.
    Отступы: 4 пробела на уровень вложенности.
    """
    indent = "    "
    lines = []

    for key, node in sorted(diff.items()):
        node_type = node["type"]

        if node_type == "nested":
            # Отступ для nested: 4 * (depth + 1)
            key_indent = indent * (depth + 1)
            lines.append(f"{key_indent}{key}: {{")
            lines.append(format_stylish(node["children"], depth + 1))
            lines.append(f"{key_indent}}}")

        elif node_type == "changed":
            # Отступ для +/-: 4 * depth + 2
            # (например, 2 для depth=0, 6 для depth=1)
            key_indent = indent * depth + "  "
            old_formatted = format_value(node["old_value"], depth + 1)
            new_formatted = format_value(node["new_value"], depth + 1)
            lines.append(f"{key_indent}- {key}: {old_formatted}")
            lines.append(f"{key_indent}+ {key}: {new_formatted}")

        elif node_type == "added":
            key_indent = indent * depth + "  "
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{key_indent}+ {key}: {formatted_value}")

        elif node_type == "removed":
            key_indent = indent * depth + "  "
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{key_indent}- {key}: {formatted_value}")

        elif node_type == "unchanged":
            # Отступ для unchanged: 4 * (depth + 1)
            key_indent = indent * (depth + 1)
            formatted_value = format_value(node["value"], depth + 1)
            lines.append(f"{key_indent}{key}: {formatted_value}")

    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "\n".join(lines)


def format_value(value, depth: int) -> str:
    """
    Форматирует значение для вывода в stylish формате.
    """
    if isinstance(value, dict):
        indent = "    " * depth
        lines = ["{"]
        for key, val in sorted(value.items()):
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_val}")
        lines.append(f"{indent}" + "}")
        return "\n".join(lines)

    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return value
    else:
        return str(value)
