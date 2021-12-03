from shared import get_lines_from_file


def calculate_power_consumption(lines):
    assert len(lines) > 0
    gamma_rate = []
    epsilon_rate = []

    for i in range(len(lines[0])):
        value, equal = get_most_common_value_in_column(i, lines)
        if value == "0":
            gamma_rate.append("0")
            epsilon_rate.append("1")
        else:
            gamma_rate.append("1")
            epsilon_rate.append("0")

    return int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)


def get_most_common_value_in_column(column, lines):
    count_of_ones = 0
    for line in lines:
        if line[column] == "1":
            count_of_ones += 1

    if count_of_ones == len(lines) / 2:
        return "1", True

    elif count_of_ones > len(lines) / 2:
        return "1", False

    else:
        return "0", False


def calculate_life_support_rating(lines):
    oxygen_rating = calculate_rating_using_filter(lines, oxygen_policy_filter)
    co2_rating = calculate_rating_using_filter(lines, co2_policy_filter)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


def calculate_rating_using_filter(lines, filter_numbers):
    numbers = lines
    column = 0

    while len(numbers) != 1:
        value, equal = get_most_common_value_in_column(column, numbers)
        numbers = filter_numbers(value, equal, numbers, column)
        column += 1

    return numbers[0]


def oxygen_policy_filter(value, equal, numbers, column):
    filtered_numbers = []

    if equal:
        value = "1"

    for number in numbers:
        if number[column] == value:
            filtered_numbers.append(number)

    return filtered_numbers


def co2_policy_filter(value, equal, numbers, column):
    filtered_numbers = []

    if equal:
        value = "0"
    elif value == "0":
        value = "1"
    elif value == "1":
        value = "0"

    for number in numbers:
        if number[column] == value:
            filtered_numbers.append(number)

    return filtered_numbers


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day3.txt")

    print(calculate_power_consumption(lines))
    print(calculate_life_support_rating(lines))
