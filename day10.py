from shared import get_lines_from_file

OPEN_CHAR = ["(", "[", "{", "<"]
VALID_PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPTED_CHAR_SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}

INCOMPLETE_CHAR_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}


def is_incomplete(line):
    stack = []
    for curr_char in line:
        if curr_char in OPEN_CHAR:
            stack.append(curr_char)
        else:
            if len(stack) == 0:
                return False
            open_char = stack.pop()
            if not is_valid_pair(open_char, curr_char):
                return False
    return len(stack) > 0


def is_corrupted(line):
    stack = []
    for curr_char in line:
        if curr_char in OPEN_CHAR:
            stack.append(curr_char)
        else:
            if len(stack) == 0:
                return True
            open_char = stack.pop()
            if not is_valid_pair(open_char, curr_char):
                return True
    return False


def is_valid_pair(open_char, close_char):
    return close_char == VALID_PAIRS[open_char]


def get_first_corrupted_char(line):
    stack = []
    for curr_char in line:
        if curr_char in OPEN_CHAR:
            stack.append(curr_char)
        else:
            if len(stack) == 0:
                return curr_char
            open_char = stack.pop()
            if not is_valid_pair(open_char, curr_char):
                return curr_char


def calculate_corrupted_syntax_score(lines):
    result = 0
    for line in lines:
        if is_corrupted(line):
            char = get_first_corrupted_char(line)
            assert char
            result += CORRUPTED_CHAR_SCORES[char]
    return result


def get_characters_to_complete(line):
    result = []
    stack = []
    for curr_char in line:
        if curr_char in OPEN_CHAR:
            stack.append(curr_char)
        else:
            open_char = stack.pop()

    assert len(stack) > 0
    for _ in range(len(stack)):
        char = stack.pop()
        result.append(VALID_PAIRS[char])
    return "".join(result)


def calculate_incomplete_syntax_scores(lines):
    result = []
    for line in lines:
        if is_incomplete(line):
            chars_to_complete = get_characters_to_complete(line)
            assert len(chars_to_complete) > 0
            line_result = 0
            for char in chars_to_complete:
                line_result = (line_result * 5) + INCOMPLETE_CHAR_SCORES[char]
            result.append(line_result)
    return result


def find_winning_incomplete_score(lines):
    scores = calculate_incomplete_syntax_scores(lines)

    # assert odd
    assert len(scores) % 2 == 1

    sorted_scores = sorted(scores)
    middle = int(len(sorted_scores) / 2)
    return sorted_scores[middle]


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day10.txt")

    print(calculate_corrupted_syntax_score(lines))
    print(find_winning_incomplete_score(lines))
