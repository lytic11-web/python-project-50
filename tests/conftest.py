import os

import pytest


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "test_data", file_name)


def read_fixture(file_name):
    path = get_fixture_path(file_name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


@pytest.fixture
def flat_json1_path():
    return get_fixture_path("flat/file1.json")


@pytest.fixture
def flat_json2_path():
    return get_fixture_path("flat/file2.json")


@pytest.fixture
def expected_stylish():
    return read_fixture("flat/expected_stylish.txt")


@pytest.fixture
def expected_plain():
    return read_fixture("flat/expected_plain.txt")


@pytest.fixture
def expected_json_flat():
    return read_fixture("flat/expected_json.txt")


@pytest.fixture
def flat_yaml1_path():
    return get_fixture_path("flat/file1.yml")


@pytest.fixture
def flat_yaml2_path():
    return get_fixture_path("flat/file2.yml")


@pytest.fixture
def nested_json1_path():
    return get_fixture_path("nested/file1.json")


@pytest.fixture
def nested_json2_path():
    return get_fixture_path("nested/file2.json")


@pytest.fixture
def expected_json_nested():
    return read_fixture("nested/expected_json.txt")


@pytest.fixture
def nested_yaml1_path():
    return get_fixture_path("nested/file1.yml")


@pytest.fixture
def nested_yaml2_path():
    return get_fixture_path("nested/file2.yml")


@pytest.fixture
def expected_nested_stylish():
    return read_fixture("nested/expected_stylish.txt")


@pytest.fixture
def expected_nested_plain():
    return read_fixture("nested/expected_plain.txt")
