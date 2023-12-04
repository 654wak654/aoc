with open("1-input.txt", "r") as input:
    lines = input.readlines()

total = 0

for line in lines:
    first_digit = -1
    last_digit = -1

    for char in line:
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            last_digit = char

            if first_digit == -1:
                first_digit = char

    total += int(first_digit + last_digit)

print(total)
