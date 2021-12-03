const input = require('./input.json');
const data = input.data;

const getMostCommon = (list, index, measurement) => {
    let mostCommon = -1;
    let countZero = 0;
    let countOne = 0;
    let binaryList = [];
    list.forEach((item) => {
        binaryList.push(item.charAt(index));
    });
    binaryList.forEach((item) => {
        if (item === '0') {
            countZero++;
        } else {
            countOne++;
        }
    });
    if (countZero > countOne) {
        mostCommon = measurement === 'co2' ? 1 : 0;
    }
    if (countOne > countZero) {
        mostCommon = measurement === 'co2' ? 0 : 1;
    }
    return mostCommon;
};

const exerciceOne = () => {
    let gammaRate = '';
    let epsilonRate = '';
    for (let i = 0; i < data[0].length; i++) {
        let mostCommon = getMostCommon(data, i)
        if (mostCommon === 0) {
            gammaRate = gammaRate + '0'
            epsilonRate = epsilonRate + '1'
        } else {
            gammaRate = gammaRate + '1'
            epsilonRate = epsilonRate + '0'
        }
    };
    console.log(parseInt(gammaRate, 2) * parseInt(epsilonRate, 2));
};

const exerciseTwo = () => {
    console.log(getLifeSupportValue('oxygen') * getLifeSupportValue('co2'));
};

const getLifeSupportValue = (measurement) => {
    let stringIndex = 0;
    let newData = data;
    while (newData.length != 1) {
        newData = getBinaryList(newData, stringIndex, measurement);
        stringIndex++;
    }
    return parseInt(newData[0], 2);
};

const getBinaryList = (list, stringIndex, measurement) => {
    let newData = [];
    let measurementValue = -1;
    measurement === 'oxygen' ? measurementValue = getMostCommon(list, stringIndex, 'oxygen') : measurementValue = getMostCommon(list, stringIndex, 'co2');  
    list.forEach((item) => {
        switch (measurementValue) {
            case 1:
                if (item.charAt(stringIndex) === '1') {
                    newData.push(item);
                }
                break;
            case 0:
                if (item.charAt(stringIndex) === '0') {
                    newData.push(item);
                }
                break;
            case -1:
                if (measurement === 'oxygen' && item.charAt(stringIndex) === '1') {
                    newData.push(item);
                }
                if (measurement === 'co2' && item.charAt(stringIndex) === '0') {
                    newData.push(item);
                }
                break;
        }
    });
    return newData;
}

exerciceOne();
exerciseTwo();