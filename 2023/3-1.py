with open("3-input.txt", "r") as f:
    lines = f.readlines()

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

total = 0
counted_indexes = []


def find_num_at_index(line_index, char_index):
    if (line_index, char_index) in counted_indexes:
        return 0

    if lines[line_index][char_index] in digits:
        counted_indexes.append((line_index, char_index))

        char_index_left = char_index - 1
        char_index_right = char_index + 1

        while lines[line_index][char_index_left] in digits:
            counted_indexes.append((line_index, char_index_left))

            char_index_left -= 1

        while lines[line_index][char_index_right] in digits:
            counted_indexes.append((line_index, char_index_right))

            char_index_right += 1

        return int(lines[line_index][char_index_left + 1 : char_index_right])

    return 0

for line_index, line in enumerate(lines):
    for char_index, char in enumerate(line):
        if char in ["*", "#", "+", "$", "%", "-", "/", "@", "=", "&"]:
            total += find_num_at_index(line_index - 1, char_index - 1) # top_left
            total += find_num_at_index(line_index - 1, char_index) # top
            total += find_num_at_index(line_index - 1, char_index + 1) # top_right
            total += find_num_at_index(line_index, char_index - 1) # left
            total += find_num_at_index(line_index, char_index + 1) # right
            total += find_num_at_index(line_index + 1, char_index - 1) # bottom_left
            total += find_num_at_index(line_index + 1, char_index) # bottom
            total += find_num_at_index(line_index + 1, char_index + 1) # bottom_right

print(total)
