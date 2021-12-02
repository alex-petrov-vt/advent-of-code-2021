from day1 import count_num_of_increases, count_num_of_increases_avg_3


def test_day_1():
    testcases = [
        {
            "name": "a single measurement should not have any increases",
            "input": [199],
            "expected": 0,
        },
        {
            "name": "a typical list of measurements should return correct number of increases",
            "input": [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
            "expected": 7,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = count_num_of_increases(test["input"])
        assert result == test["expected"]


def test_day_2():
    testcases = [
        {
            "name": "a typical list of measurements should return correct number of increases using average of 3 numbers at a time",
            "input": [199, 200, 208, 210, 200, 207, 240, 269, 260, 263],
            "expected": 5,
        },
    ]

    for test in testcases:
        print(f"Running {test['name']}")
        result = count_num_of_increases_avg_3(test["input"])
        assert result == test["expected"]
