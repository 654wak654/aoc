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

distances = 0

for i in range(len(galaxies)):
    galaxy = galaxies[i]

    for other_galaxy in galaxies[i + 1 :]:
        x_ranges = range(
            min(other_galaxy[0], galaxy[0]), max(other_galaxy[0], galaxy[0])
        )
        x_range = sum([(1000000 if x in erows else 1) for x in x_ranges])

        y_ranges = range(
            min(other_galaxy[1], galaxy[1]), max(other_galaxy[1], galaxy[1])
        )
        y_range = sum([(1000000 if x in ecolumns else 1) for x in y_ranges])

        distances += x_range + y_range

print(distances)
