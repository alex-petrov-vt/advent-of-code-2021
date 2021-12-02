from day2 import determine_destination, determine_destination_ver_2


def test_day_2():
    testcases = [
        {
            "name": "a typical series of commands",
            "input": [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ],
            "expected": 150,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = determine_destination(test["input"])
        assert result == test["expected"]


def test_day_2_part_2():
    testcases = [
        {
            "name": "a typical series of commands",
            "input": [
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ],
            "expected": 900,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = determine_destination_ver_2(test["input"])
        assert result == test["expected"]
