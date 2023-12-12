from itertools import product

with open("12-input.txt", "r") as input:
    lines = input.readlines()


# Took this function from stackoverflow so kinda cheating?
# https://stackoverflow.com/a/69792469
def fill_unknowns(s, chars):
    for p in map(iter, product(chars, repeat=s.count("?"))):
        yield "".join(c if c != "?" else next(p) for c in s)


def is_valid_for_counts(line: str, counts):
    line_simple = line.replace("?", " ").split(" ")

    return [len(x) for x in line_simple if x != ""] == counts


total = 0

for line in lines:
    spring_groups = [x for x in line.split(" ")[0].split(".") if x]
    counts = [int(x) for x in line.split(" ")[1][:-1].split(",")]

    for permutation in fill_unknowns(" ".join(spring_groups), "?#"):
        if is_valid_for_counts(permutation, counts):
            total += 1

print(total)
