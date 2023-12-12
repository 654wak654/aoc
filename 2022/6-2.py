with open("6-input.txt", "r") as input:
    inn = input.read()

for i in range(len(inn)):
    next_14_chars = inn[i : i + 14]

    if len(set(next_14_chars)) == 14:
        print(i + 14)

        break
