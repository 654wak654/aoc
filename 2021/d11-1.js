const text = document.querySelector("pre").innerText;
const input = text.split("\n").map(x => x.split("").map(y => parseInt(y)));
input.pop();

function getAdjacentEnergy(i, j) {
    if (i > -1 && i < input.length && j > -1 && j < input[i].length) {
        return input[i][j];
    }

    return null;
}

function collectAdjacents(i, j) {
    const adjacents = [
        { i: i - 1, j: j, val: getAdjacentEnergy(i - 1, j) },
        { i: i, j: j - 1, val: getAdjacentEnergy(i, j - 1) },
        { i: i, j: j + 1, val: getAdjacentEnergy(i, j + 1) },
        { i: i + 1, j: j, val: getAdjacentEnergy(i + 1, j) },
        { i: i + 1, j: j + 1, val: getAdjacentEnergy(i + 1, j + 1) },
        { i: i - 1, j: j - 1, val: getAdjacentEnergy(i - 1, j - 1) },
        { i: i + 1, j: j - 1, val: getAdjacentEnergy(i + 1, j - 1) },
        { i: i - 1, j: j + 1, val: getAdjacentEnergy(i - 1, j + 1) }
    ];

    return adjacents.filter(x => x.val !== null);
}

function light(i, j, lits) {
    const val = ++input[i][j];
    if (val > 9 && !lits.some(l => l.i === i && l.j === j)) {
        lits.push({ i, j });

        const adjacents = collectAdjacents(i, j);
        for (const adjacent of adjacents) {
            light(adjacent.i, adjacent.j, lits);
        }
    }
}

let total = 0;

for (let step = 0; step < 100; step++) {
    const lits = [];

    for (let i = 0; i < input.length; i++) {
        for (let j = 0; j < input[i].length; j++) {
            light(i, j, lits);
        }
    }

    total += lits.length;

    for (const lit of lits) {
        input[lit.i][lit.j] = 0;
    }
}

console.log(total);
