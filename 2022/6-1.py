with open("6-input.txt", "r") as input:
    inn = input.read()

for i in range(len(inn)):
    next_4_chars = inn[i : i + 4]

    if len(set(next_4_chars)) == 4:
        print(i + 4)

        break
