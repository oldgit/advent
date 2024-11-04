import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

POSSIBLE_NUMBERS = {"red": 12, "green": 13, "blue": 14}


def is_possible(sets):
    for set_cubes in sets.split("; "):
        for cubes in set_cubes.split(", "):
            (n, c) = cubes.split(" ")
            if int(n) > POSSIBLE_NUMBERS[c]:
                return False
    return True


def game_power(sets):
    colour_to_number = {"red": 0, "green": 0, "blue": 0}
    for set_cubes in sets.split("; "):
        for cubes in set_cubes.split(", "):
            (n, c) = cubes.split(" ")
            old = colour_to_number[c]
            colour_to_number[c] = max(int(n), old)
    result = 1
    for k in colour_to_number:
        result = result * colour_to_number[k]
    return result


game_sum = 0
total_power = 0
with open(f"{DAY}/input.txt", "r") as file:
    for line in file.read().splitlines():
        (game, sets_in) = line.split(": ")
        game_number = int(game.split(" ")[1])
        if is_possible(sets_in):
            game_sum = game_sum + game_number
        total_power = total_power + game_power(sets_in)

p1_expected, p2_expected = expected_for_day(DAY)
assert game_sum == p1_expected
assert total_power == p2_expected
print(f"{DAY} Part 1: {game_sum}")
print(f"{DAY} Part 2: {total_power}")
