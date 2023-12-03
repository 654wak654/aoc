const text = document.querySelector("pre").innerText;
const input = text.split("\n");
input.pop();

const map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
};

const scoreMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
};

let score = 0;

for (const line of input) {
    let expected = '';
    const topStack = [];

    for (const char of line.split("")) {
        if (char in map) {
            expected = map[char];
            topStack.push(char);
        } else if (char === expected) {
            topStack.pop();
            expected = map[topStack[topStack.length - 1]];
        } else {
            score += scoreMap[char];

            break;
        }
    }
}

console.log(score);
