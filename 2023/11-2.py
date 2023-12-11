with open("11-input.txt", "r") as input:
    lines = input.readlines()

image = []

# Expand rows
for line in lines:
    image.append(line[:-1])

    if all(x == "." for x in line[:-1]):
        # TODO: Keep a list of expanded rows
        image.append(line[:-1])

# Expand columns
indexes = []

for char_index in range(len(image[0])):
    if all(l[char_index] == "." for l in image):
        indexes.append(char_index)

for char_index in reversed(indexes):
    for i in range(len(image)):
        # TODO: Keep a list of expanded columns
        image[i] = image[i][:char_index] + "." + image[i][char_index:]

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
        distances += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(distances)
