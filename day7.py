from shared import get_lines_from_file


def select_horizontal_position(positions):
    median = find_median(positions)
    fuel_cost = 0
    for position in positions:
        fuel_cost += abs(position - median)
    return fuel_cost


def select_horizontal_position_part_2(positions):
    min_pos, max_pos = min(positions), max(positions)

    min_fuel_cost = float("inf")
    for i in range(min_pos, max_pos + 1):
        curr_fuel_cost = 0
        for position in positions:
            curr_fuel_cost += calculate_move_fuel_cost(position, i)
        min_fuel_cost = min(min_fuel_cost, curr_fuel_cost)

    return int(min_fuel_cost)


def calculate_move_fuel_cost(pos1, pos2):
    distance = abs(pos1 - pos2)
    return distance * (distance + 1) / 2


def find_median(positions):
    sorted_positions = sorted(positions)
    if len(sorted_positions) % 2 == 1:
        return sorted_positions[int(len(sorted_positions) / 2)]
    else:
        middle = int(len(sorted_positions) / 2)
        return int((sorted_positions[middle] + sorted_positions[middle - 1]) / 2)


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day7.txt")
    assert len(lines) == 1

    positions_as_str = lines[0].strip().split(",")
    positions = list(map(int, positions_as_str))

    print(select_horizontal_position(positions))
    print(select_horizontal_position_part_2(positions))
