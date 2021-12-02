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
        if (index <= measurements.length-2) {
            let result = item + measurements[index + 1] + measurements[index + 2];
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
