import json
import tempfile

import pytest

from gendiff import generate_diff


def test_generate_diff_flat_yaml(
    flat_yaml1_path, flat_yaml2_path, expected_stylish
):
    """Test flat YAML comparison with stylish format."""
    result = generate_diff(flat_yaml1_path, flat_yaml2_path)
    assert result == expected_stylish


def test_generate_diff_flat_yaml_with_format(flat_yaml1_path, flat_yaml2_path):
    """Test flat YAML comparison with explicit format."""
    result = generate_diff(flat_yaml1_path, flat_yaml2_path, "stylish")
    assert "follow: false" in result
    assert "host: hexlet.io" in result
    assert "timeout: 50" in result
    assert "timeout: 20" in result
    assert "verbose: true" in result


def test_generate_diff_flat_json(
    flat_json1_path, flat_json2_path, expected_stylish
):
    """Test flat JSON comparison with stylish format."""
    result = generate_diff(flat_json1_path, flat_json2_path)
    assert result == expected_stylish


def test_generate_diff_flat_json_with_format(flat_json1_path, flat_json2_path):
    """Test flat JSON comparison with explicit format."""
    result = generate_diff(flat_json1_path, flat_json2_path, "stylish")
    assert "follow: false" in result
    assert "host: hexlet.io" in result
    assert "timeout: 50" in result
    assert "timeout: 20" in result
    assert "verbose: true" in result


def test_generate_diff_plain_format_flat(
    flat_json1_path, flat_json2_path, expected_plain
):
    """Test plain format with flat data."""
    result = generate_diff(flat_json1_path, flat_json2_path, "plain")
    assert result == expected_plain


def test_generate_diff_plain_format_nested(
    nested_json1_path, nested_json2_path, expected_nested_plain
):
    """Test plain format with nested data."""
    result = generate_diff(nested_json1_path, nested_json2_path, "plain")
    assert result == expected_nested_plain


def test_generate_diff_json_format(flat_json1_path, flat_json2_path):
    """Test JSON format output."""
    result = generate_diff(flat_json1_path, flat_json2_path, "json")
    assert isinstance(result, str)
    assert result  # Not empty
    # Проверяем, что это валидный JSON
    json.loads(result)


def test_generate_diff_nested_json(
    nested_json1_path, nested_json2_path, expected_nested_stylish
):
    """Test nested JSON comparison with stylish format."""
    result = generate_diff(nested_json1_path, nested_json2_path)
    assert result == expected_nested_stylish


def test_generate_diff_nested_yaml(
    nested_yaml1_path, nested_yaml2_path, expected_nested_stylish
):
    """Test nested YAML comparison with stylish format."""
    result = generate_diff(nested_yaml1_path, nested_yaml2_path)
    assert result == expected_nested_stylish


def test_generate_diff_json_format_nested(
    nested_json1_path, nested_json2_path, expected_json_nested
):
    """Test JSON format output with nested data."""
    result = generate_diff(nested_json1_path, nested_json2_path, "json")
    
    # Сравниваем как строки (с учетом форматирования)
    assert result == expected_json_nested
    
    # Дополнительно проверяем, что это валидный JSON
    parsed_result = json.loads(result)
    parsed_expected = json.loads(expected_json_nested)
    
    # И что структуры совпадают
    assert parsed_result == parsed_expected


def test_unsupported_file_format():
    """Test error for unsupported file format."""
    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w") as f1:
        f1.write("some text")
        f1.flush()

        with tempfile.NamedTemporaryFile(suffix=".txt", mode="w") as f2:
            f2.write("other text")
            f2.flush()

            with pytest.raises(ValueError, match="Unsupported file format"):
                generate_diff(f1.name, f2.name)


def test_unsupported_output_format(flat_json1_path, flat_json2_path):
    """Test error for unsupported output format."""
    with pytest.raises(ValueError, match="Unsupported format"):
        generate_diff(flat_json1_path, flat_json2_path, "html")


def test_cli_script_import():
    """Test that CLI script can be imported."""
    from gendiff.scripts.gendiff import main

    assert callable(main)
