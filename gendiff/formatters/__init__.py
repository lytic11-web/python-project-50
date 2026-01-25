from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name):
    """
    Возвращает функцию-форматтер по имени формата.

    Args:
        format_name: имя формата ('stylish', 'plain', 'json')

    Returns:
        Функция-форматтер
    """
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
    }

    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")

    return formatters[format_name]
