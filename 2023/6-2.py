# example_race = (71530, 940200)
race = (52947594, 426137412791216)

wins = 0

# Hold for up to x secs
for i in range(1, race[0]):
    dist = (race[0] - i) * i

    if dist > race[1]:
        wins += 1

print(wins)
