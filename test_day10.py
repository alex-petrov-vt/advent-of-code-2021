from day10 import (
    is_corrupted,
    get_first_corrupted_char,
    calculate_corrupted_syntax_score,
    is_incomplete,
    get_characters_to_complete,
    calculate_incomplete_syntax_scores,
    find_winning_incomplete_score,
)


def test_is_corrupted_function():
    tests = [
        {"input": "{([(<{}[<>[]}>{[]{[(<()>", "expected": True},
        {"input": "[[<[([]))<([[{}[[()]]]", "expected": True},
        {"input": "[{[{({}]{}}([{[{{{}}([]", "expected": True},
        {"input": "[<(<(<(<{}))><([]([]()", "expected": True},
        {"input": "<{([([[(<>()){}]>(<<{{", "expected": True},
        {"input": "([{<>}])", "expected": False},
        {"input": "", "expected": False},
    ]

    for test in tests:
        assert test["expected"] == is_corrupted(test["input"])


def test_get_first_corrupted_char():
    tests = [
        {"input": "{([(<{}[<>[]}>{[]{[(<()>", "expected": "}"},
        {"input": "[[<[([]))<([[{}[[()]]]", "expected": ")"},
        {"input": "[{[{({}]{}}([{[{{{}}([]", "expected": "]"},
        {"input": "[<(<(<(<{}))><([]([]()", "expected": ")"},
        {"input": "<{([([[(<>()){}]>(<<{{", "expected": ">"},
    ]

    for test in tests:
        assert test["expected"] == get_first_corrupted_char(test["input"])


def test_calculate_corrupted_syntax_score():
    input = [
        "{([(<{}[<>[]}>{[]{[(<()>",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
    ]

    assert 26397 == calculate_corrupted_syntax_score(input)


def test_is_incomplete_function():
    tests = [
        {"input": "[({(<(())[]>[[{[]{<()<>>", "expected": True},
        {"input": "[(()[<>])]({[<{<<[]>>(", "expected": True},
        {"input": "(((({<>}<{<{<>}{[]{[]{}", "expected": True},
        {"input": "{<[[]]>}<{[{[{[]{()[[[]", "expected": True},
        {"input": "<{([{{}}[<[[[<>{}]]]>[]]", "expected": True},
        {"input": "([{<>}])", "expected": False},
        {"input": "", "expected": False},
    ]

    for test in tests:
        assert test["expected"] == is_incomplete(test["input"])


def test_get_characters_to_complete():
    tests = [
        {"input": "[({(<(())[]>[[{[]{<()<>>", "expected": "}}]])})]"},
        {"input": "[(()[<>])]({[<{<<[]>>(", "expected": ")}>]})"},
        {"input": "(((({<>}<{<{<>}{[]{[]{}", "expected": "}}>}>))))"},
        {"input": "{<[[]]>}<{[{[{[]{()[[[]", "expected": "]]}}]}]}>"},
        {"input": "<{([{{}}[<[[[<>{}]]]>[]]", "expected": "])}>"},
    ]

    for test in tests:
        assert test["expected"] == get_characters_to_complete(test["input"])


def test_calculate_incomplete_syntax_score():
    input = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "(((({<>}<{<{<>}{[]{[]{}",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    assert [288957, 5566, 1480781, 995444, 294] == calculate_incomplete_syntax_scores(
        input
    )


def test_calculate_winning_incomplete_score():
    input = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "(((({<>}<{<{<>}{[]{[]{}",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    assert 288957 == find_winning_incomplete_score(input)
