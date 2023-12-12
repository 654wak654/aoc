with open("4-input.txt", "r") as input:
    lines = input.readlines()

total = 0

for line in lines:
    elf_a = line.split(",")[0].split("-")
    elf_b = line.split(",")[1][:-1].split("-")  # Ignore newline

    # Even simpler than checking subset
    if int(elf_a[0]) <= int(elf_b[1]) and int(elf_a[1]) >= int(elf_b[0]):
        total += 1

print(total)
