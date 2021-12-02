from shared import get_lines_from_file, convert_lines_to_ints


def count_num_of_increases(items):
    increases = 0
    for i in range(1, len(items)):
        if items[i] > items[i - 1]:
            increases += 1

    return increases


def count_num_of_increases_avg_3(items):
    increases = 0
    for i in range(2, len(items) - 1):
        prev_sum = items[i - 2] + items[i - 1] + items[i]
        next_sum = items[i - 1] + items[i] + items[i + 1]
        if next_sum > prev_sum:
            increases += 1

    return increases


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day1.txt")
    input_nums = convert_lines_to_ints(lines)

    print(count_num_of_increases(input_nums))
    print(count_num_of_increases_avg_3(input_nums))
