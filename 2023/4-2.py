with open("4-input.txt", "r") as input:
    cards = input.readlines()

total = 0
card_counts = {i: 1 for i in range(len(cards))}

for card_index, card in enumerate(cards):
    winning_numbers = card.split("|")[0].split(":")[1].split(" ")
    our_numbers = card.split("|")[1].split(" ")

    win_count = 0

    for number in our_numbers:
        if number == "":
            continue

        if number[-1] == "\n":
            number = number[:-1]

        if number in winning_numbers:
            win_count += 1

    for i in range(card_index + 1, card_index + 1 + win_count):
        card_counts[i] += 1 * card_counts[card_index]

print(card_counts)
print(sum(card_counts.values()))
