const text = document.querySelector("pre").innerText;
const input = text.split("\n");
input.pop();

const coords = {};

for (const line of input) {
    const eh = line.split(" -> ");
    const [x1, y1] = eh[0].split(",").map(x => parseInt(x));
    const [x2, y2] = eh[1].split(",").map(x => parseInt(x));

    const xMin = Math.min(x1, x2);
    const xMax = Math.max(x1, x2);
    const yMin = Math.min(y1, y2);
    const yMax = Math.max(y1, y2);

    if (xMin !== xMax && yMin !== yMax) {
        continue;
    }

    for (let x = xMin; x < xMax + 1; x++) {
        for (let y = yMin; y < yMax + 1; y++) {
            const coord = `${x},${y}`;

            if (coord in coords) {
                coords[coord]++;
            } else {
                coords[coord] = 1;
            }
        }
    }
}

console.log(Object.values(coords).reduce((total, coordCount) => coordCount > 1 ? ++total : total, 0))
