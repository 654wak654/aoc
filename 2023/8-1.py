from re import split

with open("8-input.txt", "r") as f:
    lines = f.readlines()

instructions = lines[0][:-1]

node_map = {}

for line in lines[2:]:
    split_line = split(r"\W+", line)

    node_map[split_line[0]] = {"L": split_line[1], "R": split_line[2]}

current = "AAA"
total = 0

while current != "ZZZ":
    for i, c in enumerate(instructions):
        current = node_map[current][c]
        total += 1

        if current == "ZZZ":
            break

print(total)
