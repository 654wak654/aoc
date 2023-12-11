with open("9-input.txt", "r") as input:
    lines = input.readlines()


def history(items):
    sequence = [items[i + 1] - items[i] for i in range(len(items) - 1)]

    if any(x != 0 for x in sequence):
        sequence.insert(0, sequence[0] - history(sequence))

    return sequence[0]


total = 0

for line in lines:
    items = [int(x) for x in line[:-1].split(" ")]

    total += items[0] - history(items)

print(total)
