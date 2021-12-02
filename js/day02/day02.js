const input = require('./input.json');
const data = input.data;

const exerciseOne = () => {
    let directions = data;
    let horizontal = 0;
    let depth = 0;
    directions.forEach((item) =>  {
        let command = item.split(' ')[0];
        let value = Number(item.split(' ')[1]);
        if (command === 'forward') {
            horizontal = horizontal + value;
        } else if (command === 'down') {
            depth = depth + value;
        } else {
            depth = depth - value;
        }
    });
    console.log('current position: ' + horizontal + ' - ' + depth);
    console.log('multiplied: ' + horizontal * depth);
};

const exerciseTwo = () => {
    let directions = data;
    let horizontal = 0;
    let aim = 0;
    let depth = 0;
    directions.forEach(function(item) {
        let command = item.split(' ')[0];
        let value = Number(item.split(' ')[1]);
        switch (command) {
            case 'forward':
                horizontal = horizontal + value;
                depth = depth + ((aim || 0) * value);
                break;
            case 'down':
                aim = aim + value;
                break;
            case 'up':
                aim = aim - value;
                break;
        }
    });
    console.log('current position: ' + horizontal + ' - ' + depth);
    console.log('multiplied: ' + horizontal * depth);
};

exerciseOne();
exerciseTwo();