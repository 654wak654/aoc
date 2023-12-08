from math import lcm
from re import split

with open("8-input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0][:-1]

node_map = {}

for line in lines[2:]:
    split_line = split(r"\W+", line)

    node_map[split_line[0]] = {"L": split_line[1], "R": split_line[2]}

totals = []

for start in [x for x in node_map.keys() if x[-1] == "A"]:
    current = start
    total = 0

    while current[-1] != "Z":
        for i, c in enumerate(instructions):
            current = node_map[current][c]
            total += 1

            if current[-1] == "Z":
                break

    totals.append(total)

print(lcm(*totals))
