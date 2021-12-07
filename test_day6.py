from day6 import calculate_number_of_fish


def test_calculate_total_number_of_fish():
    day0 = [3, 4, 3, 1, 2]
    total_fish = calculate_number_of_fish(day0, 80)
    assert total_fish == 5934
    total_fish = calculate_number_of_fish(day0, 256)
    assert total_fish == 26984457539
