def expected_for_day(day):
    with open(f"{day}/expected.txt", "r") as file:
        expected = file.read().splitlines()
        return int(expected[0].split()[1]), int(expected[1].split()[1])
