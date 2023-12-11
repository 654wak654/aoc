from os import cpu_count
from concurrent.futures import ProcessPoolExecutor, as_completed

with open("5-input.txt", "r") as f:
    lines = f.readlines()

seeds = lines[0].split(":")[1][1:-1].split(" ")
maps = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}

map_name = "seed-to-soil"

for line in lines[3:]:
    # Remove newlines
    line = line[:-1]

    # Filter out empty lines
    if len(line) == 0:
        continue

    # See if this is the start of a new map definition
    first = line.split(" ")[0]
    if first in maps:
        map_name = first

        continue

    dest_range_start, source_range_start, range_length = line.split(" ")

    maps[map_name].append(
        (int(dest_range_start), int(source_range_start), int(range_length))
    )


def get_from_map(map_name, key):
    for dest_range_start, source_range_start, range_length in maps[map_name]:
        if key >= source_range_start and key <= source_range_start + range_length:
            return dest_range_start + (key - source_range_start)

    return key


def get_min_for_range(i):
    min_loc = 99999999999999999999
    base = int(seeds[i])

    for j in range(int(seeds[i + 1])):
        soil = get_from_map("seed-to-soil", base + j)
        fertilizer = get_from_map("soil-to-fertilizer", soil)
        water = get_from_map("fertilizer-to-water", fertilizer)
        light = get_from_map("water-to-light", water)
        temperature = get_from_map("light-to-temperature", light)
        humidity = get_from_map("temperature-to-humidity", temperature)
        location = get_from_map("humidity-to-location", humidity)

        if location < min_loc:
            min_loc = location

    return min_loc


with ProcessPoolExecutor(max_workers=cpu_count() - 4) as executor:
    min_location = 99999999999999999999
    futures = set()

    for i in range(0, len(seeds), 2):
        futures.add(executor.submit(get_min_for_range, i))

for future in as_completed(futures):
    result = future.result()

    if result < min_location:
        min_location = result

print(min_location)
