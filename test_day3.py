from day3 import calculate_power_consumption, calculate_life_support_rating


def test_day_3():
    testcases = [
        {
            "name": "a series of diagnostic measurements",
            "input": [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ],
            "expected": 198,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = calculate_power_consumption(test["input"])
        assert result == test["expected"]


def test_day_3_part_2():
    testcases = [
        {
            "name": "a series of diagnostic measurements",
            "input": [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ],
            "expected": 230,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = calculate_life_support_rating(test["input"])
        assert result == test["expected"]
