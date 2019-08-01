'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getAllSubstrings(str) {
    let i, j, result = [];
    for (i = 0; i < str.length; i++) {
        for (j = i + 1; j < str.length + 1; j++) {
            result.push(str.slice(i, j))
        }
    }
    return result
}


function isAnagram(str1, str2) {
    const hist = {}
    for (let i = 0; i < str1.length; i++) {
        const char = str1[i];
        hist[char] = (hist[char]) ? hist[char]+1 : 1;
 
    }
    for (let j = 0; j < str2.length; j++) {
        const char = str2[j]
        if (hist[char]) {
            hist[char]--
        } else {
            return false
        }
    }
    return true
}


function countAnagrams(currentIndex, arr) {
    const currentElement = arr[currentIndex]
    const arrRest = arr.slice(currentIndex + 1)
    let counter = 0
    for (let i = 0; i < arrRest.length; i++) {
        if (currentElement.length === arrRest[i].length && isAnagram(currentElement, arrRest[i])) {
            counter++
        }
    }
    return counter
}
// Complete the sherlockAndAnagrams function below.
function sherlockAndAnagrams(s) {

    const duplicatesCount = s.split('').filter((v, i) => s.indexOf(v) !== i).length
    if (!duplicatesCount)
        return 0
    let anagramsCount = 0
    const arr = getAllSubstrings(s)
    for (let i = 0; i < arr.length; i++) {
        anagramsCount += countAnagrams(i, arr)
    }
    return anagramsCount
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine(), 10);
    for (let qItr = 0; qItr < q; qItr++) {
        const s = readLine();
        let result = sherlockAndAnagrams(s);
        ws.write(result + "\n");
    }

    ws.end();
}
