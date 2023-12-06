# example_races = [
#     (7, 9),
#     (15, 40),
#     (30, 200),
# ]

races = [
    (52, 426),
    (94, 1374),
    (75, 1279),
    (94, 1216),
]

total = 1

for race in races:
    wins = 0

    # Hold for up to x secs
    for i in range(1, race[0]):
        dist = (race[0] - i) * i
        
        if dist > race[1]:
            wins += 1

    if wins > 0:
        total *= wins

print(total)
