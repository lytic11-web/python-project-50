import json
from typing import Any, Dict, List

from gendiff.parsers import parse_file


def read_file(file_path: str) -> Dict[str, Any]:
    """Читает и парсит JSON или YAML файлы."""
    return parse_file(file_path)


def get_diff(
    data1: Dict[str, Any], data2: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Сравнивает два плоских словаря и возвращает список различий.

    Каждый элемент списка - словарь с ключами:
    - 'key': имя ключа
    - 'value': значение
    - 'status': 'unchanged', 'added', 'removed', или 'changed'
    - 'old_value': старое значение (только для 'changed')
    """
    diff = []

    # Получаем все уникальные ключи в алфавитном порядке
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key not in data2:
            # Ключ только в первом файле (удален)
            diff.append({"key": key, "value": data1[key], "status": "removed"})
        elif key not in data1:
            # Ключ только во втором файле (добавлен)
            diff.append({"key": key, "value": data2[key], "status": "added"})
        elif data1[key] == data2[key]:
            # Ключ в обоих файлах без изменений
            diff.append(
                {"key": key, "value": data1[key], "status": "unchanged"}
            )
        else:
            # Ключ в обоих файлах, но значения разные
            diff.append(
                {
                    "key": key,
                    "value": data1[key],
                    "status": "removed",  # старое значение
                }
            )
            diff.append(
                {
                    "key": key,
                    "value": data2[key],
                    "status": "added",  # новое значение
                }
            )

    return diff


def format_stylish(diff: List[Dict[str, Any]]) -> str:
    """
    Форматирует различия в формате 'stylish'.

    Пример вывода:
    {
      - follow: false
        host: hexlet.io
      - proxy: 123.234.53.22
      - timeout: 50
      + timeout: 20
      + verbose: true
    }
    """
    lines = ["{"]

    for item in diff:
        status = item["status"]
        key = item["key"]
        value = item["value"]

        # Преобразуем булевы значения в строки
        if isinstance(value, bool):
            value = str(value).lower()
        elif value is None:
            value = "null"

        if status == "unchanged":
            lines.append(f"    {key}: {value}")
        elif status == "removed":
            lines.append(f"  - {key}: {value}")
        elif status == "added":
            lines.append(f"  + {key}: {value}")

    lines.append("}")

    return "\n".join(lines)


def generate_diff(
    file1_path: str, file2_path: str, format: str = "stylish"
) -> str:
    """
    Основная функция сравнения файлов.

    Args:
        file1_path: путь к первому файлу
        file2_path: путь ко второму файлу
        format: формат вывода (пока только 'stylish' поддерживается)

    Returns:
        Строка с различиями в указанном формате
    """
    # Читаем файлы
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)

    # Получаем различия
    diff = get_diff(data1, data2)

    # Форматируем вывод
    if format == "stylish":
        return format_stylish(diff)
    elif format == "plain":
        # Пока заглушка
        return "Plain format will be implemented later"
    elif format == "json":
        # Пока заглушка
        return json.dumps(diff, indent=2)
    else:
        raise ValueError(f"Unsupported format: {format}")
