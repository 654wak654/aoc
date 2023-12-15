with open("15-input.txt", "r") as input:
    inn = input.read()

boxes: list[dict] = []

for _ in range(256):
    boxes.append({})

for step in inn.replace("\n", "").split(","):
    if "=" in step:
        label = step.split("=")[0]
        lens = step.split("=")[1]
    else:
        label = step.split("-")[0]
        lens = None

    hash = 0

    for c in label:
        hash = (hash + ord(c)) * 17 % 256

    if lens is not None:
        boxes[hash][label] = int(lens)
    elif label in boxes[hash]:
        del boxes[hash][label]

total = 0

for box_index, box in enumerate(boxes):
    for lens_index, lens in enumerate(box.values()):
        total += (box_index + 1) * (lens_index + 1) * lens

print(total)
