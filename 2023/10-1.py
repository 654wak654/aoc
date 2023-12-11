from os import cpu_count
from concurrent.futures import ProcessPoolExecutor, as_completed

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open("10-input.txt", "r") as input:
    lines = input.readlines()

start = None
points = []
matrix = []

for line_index, line in enumerate(lines):
    top = []
    cur = []
    bot = []

    for char_index, char in enumerate(line[:-1]):
        current_index = (line_index * 3 + 1, char_index * 3 + 1)

        match char:
            case ".":
                top.extend([0, 0, 0])
                cur.extend([0, 0, 0])
                bot.extend([0, 0, 0])
            case "F":
                points.append(current_index)
                top.extend([0, 0, 0])
                cur.extend([0, 1, 1])
                bot.extend([0, 1, 0])
            case "7":
                points.append(current_index)
                top.extend([0, 0, 0])
                cur.extend([1, 1, 0])
                bot.extend([0, 1, 0])
            case "J":
                points.append(current_index)
                top.extend([0, 1, 0])
                cur.extend([1, 1, 0])
                bot.extend([0, 0, 0])
            case "|":
                points.append(current_index)
                top.extend([0, 1, 0])
                cur.extend([0, 1, 0])
                bot.extend([0, 1, 0])
            case "L":
                points.append(current_index)
                top.extend([0, 1, 0])
                cur.extend([0, 1, 1])
                bot.extend([0, 0, 0])
            case "-":
                points.append(current_index)
                top.extend([0, 0, 0])
                cur.extend([1, 1, 1])
                bot.extend([0, 0, 0])
            case "S":
                start = current_index
                top.extend([0, 1, 0])
                cur.extend([1, 1, 1])
                bot.extend([0, 1, 0])

    matrix.append(top)
    matrix.append(cur)
    matrix.append(bot)


def get_furthest_dist(point):
    grid = Grid(matrix=matrix)
    start_node = grid.node(start[0], start[1])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, _ = finder.find_path(start_node, grid.node(point[0], point[1]), grid)

    return (len(path) - 1) / 3


futures = set()

with ProcessPoolExecutor(max_workers=cpu_count() - 4) as executor:
    for point in points:
        futures.add(executor.submit(get_furthest_dist, point))

furthest_dist = 0

for future in as_completed(futures):
    result = future.result()

    if result > furthest_dist:
        furthest_dist = result

print(furthest_dist)
