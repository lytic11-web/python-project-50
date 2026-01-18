from gendiff import generate_diff


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


def test_generate_diff_plain_format(flat_json1_path, flat_json2_path):
    """Test plain format (should return stub for now)."""
    result = generate_diff(flat_json1_path, flat_json2_path, "plain")
    assert isinstance(result, str)
    assert result  # Not empty


def test_generate_diff_json_format(flat_json1_path, flat_json2_path):
    """Test JSON format (should return stub for now)."""
    result = generate_diff(flat_json1_path, flat_json2_path, "json")
    assert isinstance(result, str)
    assert result  # Not empty
