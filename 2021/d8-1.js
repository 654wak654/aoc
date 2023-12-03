const text = document.querySelector("pre").innerText;
const input = text.split("\n");
input.pop();

let uniques = 0;

for (const line of input) {
    const [_, output] = line.split(" | ").map(x => x.split(" "));

    for (const digit of output) {
        if ([2, 3, 4, 7].includes(digit.length)) {
            uniques++;
        }
    }
}

console.log(uniques);
