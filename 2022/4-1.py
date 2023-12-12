with open("4-input.txt", "r") as input:
    lines = input.readlines()


def range_subset(range1, range2):
    if len(range1) > 1 and range1.step % range2.step:
        return False

    return range1.start in range2 and range1[-1] in range2


total = 0

for line in lines:
    elf_a = line.split(",")[0].split("-")
    elf_b = line.split(",")[1][:-1].split("-")  # Ignore newline

    a_range = range(int(elf_a[0]), int(elf_a[1]) + 1)
    b_range = range(int(elf_b[0]), int(elf_b[1]) + 1)

    # Check if a contains b
    if range_subset(a_range, b_range):
        total += 1

        continue

    # Check if b contains a
    if range_subset(b_range, a_range):
        total += 1

print(total)
