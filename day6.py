import functools

from shared import get_lines_from_file


def calculate_number_of_fish(initial_state, num_of_days):
    fishes = [0 for _ in range(9)]
    for fish_age in initial_state:
        fishes[fish_age] += 1

    for _ in range(num_of_days):
        fishes_at_zero = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i + 1]

        fishes[6] += fishes_at_zero
        fishes[8] = fishes_at_zero

    return functools.reduce(lambda a, b: a + b, fishes)


if __name__ == "__main__":
    line = get_lines_from_file("./input/day6.txt")
    assert len(line) == 1
    day0_as_string = line[0].strip().split(",")
    day0 = list(map(int, day0_as_string))

    print(calculate_number_of_fish(day0, 80))
    print(calculate_number_of_fish(day0, 256))
