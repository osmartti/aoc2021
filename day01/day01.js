const input = require('./input.json');
const data = input.data;

const exerciseOne = () => {
    let measurements = data;
    let increases = 0;
    measurements.forEach((item, index) => {
        if (item > measurements[index - 1]) {
            increases++
        }
    });
    console.log(increases);
};

const exerciseTwo = () => {
    let measurements = data;
    let increases = 0;
    let windows = [];
    measurements.forEach((item, index) => {
        let secondValue = measurements[index + 1] || 0;
        let thirdValue = measurements[index + 2] || 0;
        if (secondValue > 0 && thirdValue > 0) {
            let result = item + secondValue + thirdValue;
            windows.push(result);
        }
    });
    windows.forEach((item, index) => {
        if (item < windows[index + 1]) {
            increases++;
        }
    });
    console.log(increases);
}

exerciseOne();
exerciseTwo();

