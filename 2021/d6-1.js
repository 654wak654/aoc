const text = document.querySelector("pre").innerText;
const input = text.split(",");

const fishes = input.map(x => parseInt(x));

for (let day = 0; day < 80; day++) {
    const newFishes = [];

    for (let i = 0; i < fishes.length; i++) {
        if (fishes[i] === 0) {
            fishes[i] = 7;
            newFishes.push(8);
        }

        fishes[i]--;
    }

    for (const newFish of newFishes) {
        fishes.push(newFish);
    }
}

console.log(fishes.length);
