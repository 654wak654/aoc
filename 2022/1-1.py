with open("1-input.txt", "r") as input:
    inn = input.read()

elves = inn.split("\n\n")

max_calories = 0

for elf in elves:
    calories = sum([int(x) for x in elf.split("\n") if x])

    if calories > max_calories:
        max_calories = calories

print(max_calories)
