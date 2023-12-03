const text = document.querySelector("pre").innerText;
const input = text.split("\n").map(x => x.split("").map(y => parseInt(y)));
input.pop();

let total = 0;

function getAdjacentHeight(i, j, adjacents) {
    if (i > -1 && i < input.length && j > -1 && j < input[i].length) {
        adjacents.push(input[i][j]);
    }
}

for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
        const val = input[i][j];
        const adjacents = [];
        getAdjacentHeight(i - 1, j, adjacents);
        getAdjacentHeight(i, j - 1, adjacents);
        getAdjacentHeight(i, j + 1, adjacents);
        getAdjacentHeight(i + 1, j, adjacents);

        if (adjacents.every(x => x > val)) {
            total += val + 1;
        }
    }
}

console.log(total);
