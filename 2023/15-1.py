with open("15-input.txt", "r") as input:
    inn = input.read()

total = 0

for step in inn.replace("\n", "").split(","):
    hash = 0

    for c in step:
        hash += ord(c)
        hash *= 17
        hash = hash % 256

    total += hash

print(total)
