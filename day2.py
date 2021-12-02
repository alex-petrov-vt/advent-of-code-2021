from shared import get_lines_from_file


def determine_destination(lines):
    horizontal = depth = 0
    for line in lines:
        command, value = line.strip().split(" ")

        if command == "forward":
            horizontal += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)

    return horizontal * depth


def determine_destination_ver_2(lines):
    horizontal = depth = aim = 0

    for line in lines:
        command, value = line.strip().split(" ")

        if command == "forward":
            horizontal += int(value)
            depth += int(value) * aim

        elif command == "down":
            aim += int(value)

        elif command == "up":
            aim -= int(value)

    return horizontal * depth


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day2.txt")

    print(determine_destination(lines))
    print(determine_destination_ver_2(lines))
