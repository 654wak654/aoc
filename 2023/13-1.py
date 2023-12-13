with open("13-input.txt", "r") as input:
    inn = input.read()

patterns = inn.split("\n\n")


def get_symmetry(lines):
    largest_symmetry = 0
    largest_symmetry_index = 0

    # Check symmetry from each line except left most and right most lines
    for x in range(len(lines) - 1):
        cur_symmetry = 0
        left = x
        right = x + 1
        valid = False

        # Go left and right until we run out of array to iterate
        while True:
            if lines[left] == lines[right]:
                cur_symmetry += 1
                left -= 1
                right += 1
            else:
                break

            if left == -1 or right > len(lines) - 1:
                valid = True
                break

        # Only keep the largest symmetry
        if cur_symmetry > largest_symmetry and valid:
            largest_symmetry = cur_symmetry
            largest_symmetry_index = x

    return largest_symmetry, largest_symmetry_index


total = 0

for pattern in patterns:
    lines = [list(x) for x in pattern.split("\n") if x]
    columns: list[list] = []

    # Rotate the pattern 90 degrees so I can check both for horizontal symmetry
    for x in range(len(lines[0])):
        columns.append([])

        for y in range(len(lines)):
            columns[x].append(lines[y][x])

    # Check horizontal symmetry
    symmetry_h, index_h = get_symmetry(lines)

    # Check vertical symmetry
    symmetry_v, index_v = get_symmetry(columns)

    if symmetry_h > symmetry_v:
        total += (index_h + 1) * 100
    else:
        total += index_v + 1

print(total)
