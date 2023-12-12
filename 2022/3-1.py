from string import ascii_letters

with open("3-input.txt", "r") as input:
    lines = input.readlines()

total = 0

for line in lines:
    half_length = int((len(line) - 1) / 2)

    first = line[:half_length]
    second = line[half_length:-1]  # Ignore newline with -1

    total += ascii_letters.index(set(first).intersection(second).pop()) + 1

print(total)
