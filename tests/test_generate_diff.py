from gendiff import generate_diff


def test_equvivalent():
    correct = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff("file1.json", "file2.json") == correct
