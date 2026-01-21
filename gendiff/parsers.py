"""Модуль для парсинга различных форматов файлов."""

import json
from typing import Any, Dict

import yaml


def parse_file(file_path: str) -> Dict[str, Any]:
    """
    Парсит файл в зависимости от его расширения.

    Args:
        file_path: путь к файлу

    Returns:
        Словарь с данными из файла

    Raises:
        ValueError: если формат файла не поддерживается
    """
    if file_path.endswith((".yml", ".yaml")):
        return parse_yaml(file_path)
    elif file_path.endswith(".json"):
        return parse_json(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def parse_yaml(file_path: str) -> Dict[str, Any]:
    """Парсит YAML файл."""
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def parse_json(file_path: str) -> Dict[str, Any]:
    """Парсит JSON файл."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
