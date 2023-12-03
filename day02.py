"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

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
with open("day02/input.txt", "r") as file:
    for line in file.read().splitlines():
        (game, sets) = line.split(": ")
        game_number = int(game.split(" ")[1])
        if is_possible(sets):
            game_sum = game_sum + game_number
        total_power = total_power + game_power(sets)

print("Part 1:", game_sum)
print("Part 2:", total_power)
