from day12 import build_graph, count_paths, count_paths_helper, count_paths_can_visit_twice

def test_building_graph():
    tests = [
        {
            "input": [
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ],
            "expected": {
                "start": ["A", "b"],
                "A": ["c", "b", "end"],
                "b": ["A", "d", "end"],
                "c": ["A"],
                "d": ["b"],
                "end": []
            }
        },
        {
            "input": [
                "dc-end",
                "HN-start",
                "start-kj",
                "dc-start",
                "dc-HN",
                "LN-dc",
                "HN-end",
                "kj-sa",
                "kj-HN",
                "kj-dc"
            ],
            "expected": {
                "start": ["kj", "dc", "HN"],
                "kj": ["sa", "HN", "dc"],
                "dc": ["HN", "LN", "end", "kj"],
                "HN": ["dc", "kj", "end"],
                "LN": ["dc"],
                "sa": ["kj"],
                "end": [],
            }
        },

    ]

    for test in tests:
        assert sorted(test["expected"]) == sorted(build_graph(test["input"]))

def test_finding_number_of_paths_from_start_to_end_visiting_small_caves_once():
    tests = [
        {
            "input": {
                "start": ["A", "b"],
                "A": ["c", "b", "end"],
                "b": ["A", "d", "end"],
                "c": ["A"],
                "d": ["b"],
                "end": []
            },
            "expected": 10
        },
        {
            "input": {
                "start": ["kj", "dc", "HN"],
                "kj": ["sa", "HN", "dc"],
                "dc": ["HN", "LN", "end", "kj"],
                "HN": ["dc", "kj", "end"],
                "LN": ["dc"],
                "sa": ["kj"],
                "end": [],
            },
            "expected": 19
        },
    ]

    for test in tests:
        assert test["expected"] == count_paths(test["input"])


def test_finding_number_of_paths_from_start_to_end_where_one_small_cave_can_be_visited_twice():
    tests = [
        {
            "input": {
                "start": ["A", "b"],
                "A": ["c", "b", "end"],
                "b": ["A", "d", "end"],
                "c": ["A"],
                "d": ["b"],
                "end": []
            },
            "expected": 36
        },
    ]

    for test in tests:
        assert test["expected"] == count_paths_can_visit_twice(test["input"])
