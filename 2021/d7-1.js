const text = document.querySelector("pre").innerText;
const input = text.split(",").map(x => parseInt(x));

input.sort((a, b) => a - b);

const min = input[0];
const max = input[input.length - 1];

let leastDiff = Number.MAX_SAFE_INTEGER;
let pos;

for (let i = min; i <= max; i++) {
    let diff = 0;

    for (const num of input) {
        diff += Math.abs(num - i);
    }

    if (diff < leastDiff) {
        leastDiff = diff;
        pos = i;
    }
}

console.log(leastDiff, pos);
