with open("4-input.txt", "r") as input:
    cards = input.readlines()

total = 0

for card in cards:
    winning_numbers = card.split("|")[0].split(":")[1].split(" ")
    our_numbers = card.split("|")[1].split(" ")

    points = 0

    for number in our_numbers:
        if number == "":
            continue

        if number[-1] == "\n":
            number = number[:-1]

        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    total += points

print(total)
