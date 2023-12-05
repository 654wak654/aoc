with open("2-input.txt", "r") as f:
    lines = f.readlines()

total = 0

max_red = 12
max_green = 13
max_blue = 14

for line in lines:
    game_id = int(line.split(":")[0].split(" ")[1])
    draws = line.split(":")[1].split(";")

    max_red_drawn = 0
    max_green_drawn = 0
    max_blue_drawn = 0

    for draw in draws:
        cube_counts = [x.strip() for x in draw.split(",")]

        red = next((int(x.split(" ")[0]) for x in cube_counts if "red" in x), 0)
        green = next((int(x.split(" ")[0]) for x in cube_counts if "green" in x), 0)
        blue = next((int(x.split(" ")[0]) for x in cube_counts if "blue" in x), 0)

        if red > max_red_drawn:
            max_red_drawn = red

        if green > max_green_drawn:
            max_green_drawn = green

        if blue > max_blue_drawn:
            max_blue_drawn = blue

    if (
        max_red_drawn <= max_red
        and max_green_drawn <= max_green
        and max_blue_drawn <= max_blue
    ):
        total += game_id

print(total)
