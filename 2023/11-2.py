with open("11-input.txt", "r") as input:
    lines = input.readlines()

image = []

# Expand rows
erows = []

for line_index, line in enumerate(lines):
    image.append(line[:-1])

    if all(x == "." for x in line[:-1]):
        erows.append(line_index)

# Expand columns
ecolumns = []

for char_index in range(len(image[0])):
    if all(l[char_index] == "." for l in image):
        ecolumns.append(char_index)

galaxies = []

for y in range(len(image[0])):
    for x in range(len(image)):
        if image[x][y] == "#":
            galaxies.append((x, y))

# TODO: Keep list of expanded rows/columns, add them to the diff as they come up

distances = 0

for i in range(len(galaxies)):
    galaxy = galaxies[i]

    for other_galaxy in galaxies[i + 1 :]:
        # TODO: these should be all the indexes between rn, check them against erows & ecolumns
        x_indexes = list(
            range(min(other_galaxy[0], galaxy[0]) + 1, max(other_galaxy[0], galaxy[0]))
        )

        y_indexes = list(
            range(min(other_galaxy[1], galaxy[1]) + 1, max(other_galaxy[1], galaxy[1]))
        )

print(distances)
