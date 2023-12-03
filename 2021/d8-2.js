const text = document.querySelector("pre").innerText;
const input = text.split("\n");
input.pop();

let total = 0;

for (const line of input) {
    const [signal, output] = line.split(" | ").map(x =>
        x.split(" ").map(y => y.split("").sort().join(""))
    );

    const key = {};
    const keyR = {};
    const nopeX = new Set();
    const nopeY = new Set();

    for (const x of signal.concat(output)) {
        switch (x.length) {
            case 2:
                key[x] = "1";
                keyR["1"] = x;
                break;
            case 3:
                key[x] = "7";
                keyR["7"] = x;
                break;
            case 4:
                key[x] = "4";
                keyR["4"] = x;
                break;
            case 5:
                // Either 2 or 3 or 5
                nopeX.add(x);
                break;
            case 6:
                // Either 0 or 6 or 9
                nopeY.add(x);
                break;
            case 7:
                key[x] = "8";
                break;
        }
    }

    const top = keyR["7"].split("").filter(x => !keyR["1"].includes(x))[0];
    const fourAndSeven = keyR["4"] + top;
    let bottomSegment;

    // Either 0 or 6 or 9
    for (const y of nopeY.values()) {
        const letters = y.split("").filter(x => !fourAndSeven.includes(x));

        // Find 9
        if (letters.length === 1) {
            key[y] = "9";
            bottomSegment = letters[0];
            nopeY.delete(y);

            break;
        }
    }

    // Either 2 or 3 or 5
    for (const x of nopeX.values()) {
        const letters = x.split("").filter(y => y !== bottomSegment);

        let l = null;
        for (const letter of letters) {
            if (!fourAndSeven.includes(letter)) {
                l = letter;
                break;
            }
        }

        // Find 2
        if (l !== null) {
            key[x] = "2";
            nopeX.delete(x);

            break;
        }
    }

    // Either 3 or 5
    for (const x of nopeX.values()) {
        const letters = x.split("").filter(y => !keyR["1"].includes(y));

        key[x] = letters.length === 3 ? "3" : "5";
    }

    // Either 0 or 6
    for (const y of nopeY.values()) {
        const letters = y.split("").filter(x => !keyR["1"].includes(x));

        key[y] = letters.length === 4 ? "0" : "6";
    }

    total += parseInt(output.map(digit => key[digit]).join(""));
}

console.log(total);
