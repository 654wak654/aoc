with open("2-input.txt", "r") as input:
    lines = input.readlines()

total = 0

for line in lines:
    match line[:-1]:
        case "A Y":
            total += 8
        case "B Y":
            total += 5
        case "C Y":
            total += 2
        case "A X":
            total += 4
        case "B X":
            total += 1
        case "C X":
            total += 7
        case "A Z":
            total += 3
        case "B Z":
            total += 9
        case "C Z":
            total += 6

print(total)
