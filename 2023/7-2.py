with open("7-input.txt", "r") as f:
    lines = f.readlines()

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


def get_type(hand):
    if hand == "JJJJJ":
        hand = "22222"

    unsorted_count = {}
    for c in hand:
        unsorted_count[c] = unsorted_count.setdefault(c, 0) + 1

    if unsorted_count.get("J", 0) > 0:
        most_common_count = 0
        most_common_key = None

        for key in unsorted_count:
            if key != "J" and unsorted_count[key] > most_common_count:
                most_common_count = unsorted_count[key]
                most_common_key = key

        unsorted_count[most_common_key] += unsorted_count["J"]

        del unsorted_count["J"]

    count = sorted(unsorted_count.values())

    if count[0] == 5:
        # Five of a kind
        return 6

    if len(count) == 2:
        if count[0] == 1 and count[1] == 4:
            # Four of a kind
            return 5
        else:
            # Full house
            return 4

    if len(count) == 3:
        if count[2] == 3:
            # Three of a kind
            return 3
        else:
            # Two pair
            return 2

    # No need for a len(count) == 4 check at this point
    if count[3] == 2:
        # One pair
        return 1

    # High card
    return 0


class HandComparator(tuple):
    def __lt__(self, other):
        type_diff = self[1] - other[1]

        if type_diff != 0:
            return type_diff > 0

        for i in range(5):
            self_index = cards.index(self[0][i])
            other_index = cards.index(other[0][i])

            index_diff = self_index - other_index

            if index_diff != 0:
                return index_diff > 0

        # Absolutely equal
        return False


hands = [
    (x.split(" ")[0], get_type(x.split(" ")[0]), int(x.split(" ")[1])) for x in lines
]

hands.sort(key=HandComparator, reverse=True)

total = 0

for i, hand in enumerate(hands):
    total += hand[2] * (i + 1)

print(total)
