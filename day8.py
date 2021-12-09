from shared import get_lines_from_file

NUMBER_OF_SEGMENTS = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

ORIGINAL_SEGMENT_MAPPING = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9
}

def count_ones_fours_sevens_eights(input):
    result = 0

    for line in input:
        output_value = line.strip().split('|')[1]
        output_words = output_value.split()
        for word in output_words:
            if len(word) == NUMBER_OF_SEGMENTS[1] \
                    or len(word) == NUMBER_OF_SEGMENTS[4] \
                    or len(word) == NUMBER_OF_SEGMENTS[7] \
                    or len(word) == NUMBER_OF_SEGMENTS[8]:
                result += 1

    return result

def get_one_four_seven_eight_patterns(words):
    one_pattern = four_pattern = seven_pattern = eight_pattern = ""

    for word in words:
        if len(word) == NUMBER_OF_SEGMENTS[1]:
            one_pattern = word
        elif len(word) == NUMBER_OF_SEGMENTS[4]:
            four_pattern = word
        elif len(word) == NUMBER_OF_SEGMENTS[7]:
            seven_pattern = word
        elif len(word) == NUMBER_OF_SEGMENTS[8]:
            eight_pattern = word

    return one_pattern, four_pattern, seven_pattern, eight_pattern


def find_a_wire(one, seven):
    for letter in seven:
        if letter not in one:
            return letter

def find_nine_pattern(a_wire, four, words):
    for word in words:
        if len(word) == NUMBER_OF_SEGMENTS[9]:
            is_nine = True
            extra_g_wire_used = False
            for letter in word:
                if not letter in four and letter != a_wire:
                    if not extra_g_wire_used:
                        extra_g_wire_used = True
                    else:
                        is_nine = False
                        break

            if is_nine and extra_g_wire_used:
                return word

def find_g_wire(a_wire, four, nine):
    for letter in nine:
        if letter not in four and letter != a_wire:
            return letter

def find_three_pattern(a_wire, g_wire, one, words):
    for word in words:
        if len(word) == NUMBER_OF_SEGMENTS[3]:
            is_three = True
            extra_d_wire_used = False
            for letter in word:
                if not letter in one and letter != a_wire and letter != g_wire:
                    if not extra_d_wire_used:
                        extra_d_wire_used = True
                    else:
                        is_three = False
                        break
            if is_three and extra_d_wire_used:
                return word

def find_d_wire(a_wire, g_wire, one, three):
    for letter in three:
        if letter not in one and letter != a_wire and letter != g_wire:
            return letter

def find_b_wire(d_wire, one, four):
    for letter in four:
        if letter not in one and letter != d_wire:
            return letter

def find_five_pattern(a_wire, b_wire, d_wire, g_wire, words):
    for word in words:
        if len(word) == NUMBER_OF_SEGMENTS[5]:
            is_five = True
            extra_f_wire_used = False
            for letter in word:
                if letter != a_wire and letter != b_wire and letter != d_wire and letter != g_wire:
                    if not extra_f_wire_used:
                        extra_f_wire_used = True
                    else:
                        is_five = False
                        break
            if is_five and extra_f_wire_used:
                return word

def find_f_wire(a_wire, b_wire, d_wire, g_wire, five):
    for letter in five:
        if letter != a_wire and letter != b_wire and letter != d_wire and letter != g_wire:
            return letter


def find_c_wire(f_wire, one):
    for letter in one:
        if letter != f_wire:
            return letter

def find_e_wire(a_wire, b_wire, c_wire, d_wire, f_wire, g_wire, eight):
    for letter in eight:
        if letter != a_wire and letter != b_wire and letter != c_wire and letter != d_wire and letter != f_wire and letter != g_wire:
            return letter

def decode_output_value(input):
    result = 0

    for line in input:
        input_words = line.strip().split("|")[0].split()
        output_words = line.strip().split("|")[1].split()
        wires = determine_wires(input_words)
        wire_mapping = {
            wires[0]: "a",
            wires[1]: "b",
            wires[2]: "c",
            wires[3]: "d",
            wires[4]: "e",
            wires[5]: "f",
            wires[6]: "g"
        }
        corrected_output_words = correct_output_words(wire_mapping, output_words)
        numeric_output_value = get_output_number(corrected_output_words)
        result += numeric_output_value

    return result

def determine_wires(words):
    one_pattern, four_pattern, seven_pattern, eight_pattern = get_one_four_seven_eight_patterns(words)
    a_wire = find_a_wire(one_pattern, seven_pattern)
    nine_pattern = find_nine_pattern(a_wire, four_pattern, words)
    g_wire = find_g_wire(a_wire, four_pattern, nine_pattern)
    three_pattern = find_three_pattern(a_wire, g_wire, one_pattern, words)
    d_wire = find_d_wire(a_wire, g_wire, one_pattern, three_pattern)
    b_wire = find_b_wire(d_wire, one_pattern, four_pattern)
    five_pattern = find_five_pattern(a_wire, b_wire, d_wire, g_wire, words)
    f_wire = find_f_wire(a_wire, b_wire, d_wire, g_wire, five_pattern)
    c_wire = find_c_wire(f_wire, one_pattern)
    e_wire = find_e_wire(a_wire, b_wire, c_wire, d_wire, f_wire, g_wire, eight_pattern)
    return a_wire, b_wire, c_wire, d_wire, e_wire, f_wire, g_wire


def correct_output_words(wire_mapping, output_words):
    result = []
    for word in output_words:
        corrected_word = []
        for letter in word:
            if letter in wire_mapping:
                corrected_word.append(wire_mapping[letter])
        result.append("".join(sorted(corrected_word)))
    return result

def get_output_number(output_words):
    output_value_as_string = ""
    for word in output_words:
        output_value_as_string += str(ORIGINAL_SEGMENT_MAPPING[word])
    return int(output_value_as_string)




if __name__ == "__main__":
    lines = get_lines_from_file("./input/day8.txt")

    print(count_ones_fours_sevens_eights(lines))
    print(decode_output_value(lines))
