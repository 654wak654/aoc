const text = document.querySelector("pre").innerText;
const input = text.split("\n");
// input.pop();

class Board {
    constructor(elements) {
        this.winner = false;
        this.elements = elements.filter(x => x.trim()).map(x => ({
            value: parseInt(x),
            marked: false
        }));
    }

    markAndGetScore(number) {
        for (const element of this.elements) {
            if (element.value === number) {
                element.marked = true;
                break;
            }
        }

        let victory = false;

        // Check rows
        for (let i = 0; i < this.elements.length; i += 5) {
            victory = this.elements.slice(i, i + 5).every(e => e.marked);

            if (victory) {
                break;
            }
        }

        if (!victory) {
            // Check columns
            for (let nth = 0; nth < 5; nth++) {
                victory = this.elements.slice(nth).filter((_, i) => i % 5 === 0).every(e => e.marked);

                if (victory) {
                    break;
                }
            }
        }

        if (victory) {
            this.winner = true;

            return this.elements.filter(e => !e.marked).reduce((a, b) => a + b.value, 0)
        } else {
            return 0;
        }
    }
}

const numbers = input[0].split(",").map(x => parseInt(x));
const boards = [];

const currentBoard = [];
for (let i = 2; i < input.length; i++) {
    if (input[i] === "") {
        const board = new Board(currentBoard);
        boards.push(board);

        currentBoard.length = 0;
    } else {
        currentBoard.push(...input[i].split(" "));
    }
}

(() => {
    for (const number of numbers) {
        for (const board of boards.filter(b => !b.winner)) {
            const score = board.markAndGetScore(number);

            if (score !== 0) {
                console.log(score * number);
            }
        }
    }
})();
