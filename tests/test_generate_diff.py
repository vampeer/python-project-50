import os

from gendiff import generate_diff
from gendiff.generate_diff import is_yaml, is_json


def get_case_file(filename):
    f = open(os.path.abspath("tests/test_data/" + filename), "r")
    return f.read()


def test_yaml():
    assert is_yaml("file.yaml") is True
    assert is_yaml("file.yml") is True
    assert is_yaml(".yml") is True
    assert is_yaml(".yaml") is True
    assert is_yaml("file.txt") is False
    assert is_yaml("yaml.txt") is False


def test_json():
    assert is_json("file.json") is True
    assert is_json(".json") is True
    assert is_json(".yml") is False
    assert is_json(".yaml") is False
    assert is_json("file.txt") is False
    assert is_json("yaml.txt") is False


def test_both_empty():
    assert generate_diff(
        "tests/test_data/empty.json", "tests/test_data/empty.json"
    ) == get_case_file("empty.txt")


def test_json_difference():
    assert generate_diff(
        "tests/test_data/file1.json", "tests/test_data/file2.json"
    ) == get_case_file("exercise_case.txt")


def test_yaml_difference():
    assert generate_diff(
        "tests/test_data/file1.yaml", "tests/test_data/file2.yaml"
    ) == get_case_file("exercise_case.txt")
