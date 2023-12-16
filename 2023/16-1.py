with open("16-input.txt", "r") as input:
    lines = input.readlines()

grid = []

for line in lines:
    grid.append([c for c in line[:-1]])

energized = set()
energized_with_dir = set()
beams = [[0, 0, "right"]]

while True:
    out_beams = 0
    new_beams = []

    for beam_index, beam in enumerate(beams):
        try:
            if tuple(beam) in energized_with_dir:
                raise IndexError()

            if beam[0] < 0 or beam[1] < 0:
                raise IndexError()

            current = grid[beam[0]][beam[1]]
        except IndexError:
            out_beams += 1
            continue

        energized.add((beam[0], beam[1]))
        energized_with_dir.add(tuple(beam))

        match current:
            case ".":
                pass # No need to modify direction
            case "/":
                match beam[2]:
                    case "up":
                        beam[2] = "right"
                    case "down":
                        beam[2] = "left"
                    case "left":
                        beam[2] = "down"
                    case "right":
                        beam[2] = "up"
            case "\\":
                match beam[2]:
                    case "up":
                        beam[2] = "left"
                    case "down":
                        beam[2] = "right"
                    case "left":
                        beam[2] = "up"
                    case "right":
                        beam[2] = "down"
            case "|":
                if beam[2] == "up" or beam[2] == "down":
                    pass # No need to modify direction
                else:
                    beam[2] = "up"
                    new_beams.append([beam[0], beam[1], "down"])
            case "-":
                if beam[2] == "left" or beam[2] == "right":
                    pass # No need to modify direction
                else:
                    beam[2] = "left"
                    new_beams.append([beam[0], beam[1], "right"])

        beams[beam_index][2] = beam[2]

        match beam[2]:
            case "up":
                beams[beam_index][0] -= 1
            case "down":
                beams[beam_index][0] += 1
            case "left":
                beams[beam_index][1] -= 1
            case "right":
                beams[beam_index][1] += 1

    beams.extend(new_beams)

    if out_beams == len(beams):
        break

print(len(energized))
