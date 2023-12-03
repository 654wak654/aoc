const text = document.querySelector("pre").innerText;
const input = text.split("\n").map(x => x.split("").map(y => parseInt(y)));
input.pop();

function getAdjacentHeight(i, j, ignore9) {
    if (i > -1 && i < input.length && j > -1 && j < input[i].length) {
        const val = input[i][j];
        if (!ignore9 || val !== 9) {
            return val;
        }
    }

    return null;
}

function collectAdjacents(i, j, ignore9 = false) {
    const adjacents = [
        { i: i - 1, j: j, val: getAdjacentHeight(i - 1, j, ignore9) },
        { i: i, j: j - 1, val: getAdjacentHeight(i, j - 1, ignore9) },
        { i: i, j: j + 1, val: getAdjacentHeight(i, j + 1, ignore9) },
        { i: i + 1, j: j, val: getAdjacentHeight(i + 1, j, ignore9) }
    ];

    return adjacents.filter(x => x.val !== null);
}

function gatherAllAdjacents(adjacents, touched) {
    const all = adjacents;

    for (const adjacent of adjacents) {
        let a = collectAdjacents(adjacent.i, adjacent.j, true);

        a = a.filter(aa => !touched.some(t => t.i == aa.i && t.j == aa.j));

        if (a.length > 0) {
            touched.push(...a);
            all.push(...gatherAllAdjacents(a, touched));
        }
    }

    return all;
}

const basinSizes = [];

for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
        const val = input[i][j];
        const adjacents = collectAdjacents(i, j);

        if (adjacents.every(x => x.val > val)) {
            const touched = [...adjacents, { i, j }];
            const all = gatherAllAdjacents(adjacents.filter(aa => aa.val < 9), touched);

            basinSizes.push(all.length + 1);
        }
    }
}

basinSizes.sort((a, b) => b - a);

console.log(basinSizes[0] * basinSizes[1] * basinSizes[2]);
