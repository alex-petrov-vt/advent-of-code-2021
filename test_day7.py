from day7 import select_horizontal_position, select_horizontal_position_part_2


def test_selecting_horizontal_position_part_1():
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    min_fuel = select_horizontal_position(positions)
    assert min_fuel == 37


def test_selecting_horizontal_position_part_2():
    positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    min_fuel = select_horizontal_position_part_2(positions)
    assert min_fuel == 168
