from string import ascii_letters

with open("3-input.txt", "r") as input:
    lines = input.readlines()

total = 0

for i in range(0, len(lines), 3):
    line_group = lines[i : i + 3]

    total += (
        ascii_letters.index(
            set(line_group[0][:-1])  # Enough to remove newline from just one line
            .intersection(line_group[1])
            .intersection(line_group[2])
            .pop()
        )
        + 1
    )

print(total)
