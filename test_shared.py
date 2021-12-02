from shared import get_lines_from_file, convert_lines_to_ints


def test_get_lines_from_file():
    lines = get_lines_from_file("./input/test_input.txt")
    assert lines == ["This", "is", "test", "data", "1", "541", "101"]


def test_convert_lines_to_ints():
    lines = ["1", "13", "15123"]
    nums = convert_lines_to_ints(lines)
    assert nums == [1, 13, 15123]
