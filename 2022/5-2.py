with open("5-input.txt", "r") as input:
    inn = input.read()

total = 0

drawing = inn.split("\n\n")[0]
steps = inn.split("\n\n")[1].split("\n")[:-1]

stacks: list[list] = []

for _ in range(int(drawing.split("\n")[-1].split(" ")[-2])):
    stacks.append([])

for line in reversed(drawing.split("\n")[:-1]):
    for index, column in enumerate(line.replace("    ", " ").split(" ")):
        if column:
            stacks[index].append(column)

for step in steps:
    count = int(step.split(" ")[1])
    from_stack = int(step.split(" ")[3]) - 1
    to_stack = int(step.split(" ")[5]) - 1

    stacks[to_stack].extend(stacks[from_stack][-count:])
    del stacks[from_stack][-count:]

for s in stacks:
    print(s.pop()[1], end="")

print()
