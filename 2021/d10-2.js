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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
};

const topStacks = input.map(line => {
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
            return null;
        }
    }

    return topStack;
});

const scores = [];

for (const topStack of topStacks) {
    if (topStack === null) {
        continue;
    }

    let score = 0;

    for (let i = topStack.length - 1; i >= 0; i--) {
        score *= 5;
        score += scoreMap[map[topStack[i]]];
    }

    scores.push(score);
}

scores.sort((a, b) => a - b);

console.log(scores[Math.floor(scores.length / 2)]);
