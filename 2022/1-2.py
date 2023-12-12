with open("1-input.txt", "r") as input:
    inn = input.read()

elves = inn.split("\n\n")

all_calories = []

for elf in elves:
    calories = sum([int(x) for x in elf.split("\n") if x])

    all_calories.append(calories)

print(sum(sorted(all_calories)[-3:]))
