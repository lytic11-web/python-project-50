def format_plain(diff, path=""):
    """
    Форматирует дерево различий в plain формате.

    Args:
        diff: дерево различий
        path: текущий путь к свойству

    Returns:
        Строка в формате plain
    """
    lines = []

    for key, node in sorted(diff.items()):
        current_path = f"{path}.{key}" if path else key
        node_type = node["type"]

        if node_type == "nested":
            nested_lines = format_plain(node["children"], current_path)
            if nested_lines:
                lines.append(nested_lines)

        elif node_type == "changed":
            old_value = format_plain_value(node["old_value"])
            new_value = format_plain_value(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )

        elif node_type == "added":
            value = format_plain_value(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )

        elif node_type == "removed":
            lines.append(f"Property '{current_path}' was removed")

        # unchanged не выводим в plain формате

    return "\n".join(lines)


def format_plain_value(value):
    """
    Форматирует значение для plain формата.

    Args:
        value: значение для форматирования

    Returns:
        Отформатированная строка
    """
    if isinstance(value, dict):
        return "[complex value]"

    if isinstance(value, str):
        return f"'{value}'"

    if value is None:
        return "null"

    if isinstance(value, bool):
        return str(value).lower()

    # Для чисел и других типов
    return str(value)
