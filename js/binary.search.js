'use strict';
/**
Binary Search is searching technique which works on Divide and Conquer approach. 
	It used to search any element in a sorted array.

As compared to linear, binary search is much faster with Time Complexity of O(logN) whereas linear search algorithm works in O(N) time complexity.
In this article, implement of Binary Search in Javascript using both iterative and recursive ways are discussed.
Given a sorted array of numbers. The task is to search a given element x in the array using Binary search.

Examples:
Input : arr[] = {1, 3, 5, 7, 8, 9}
        x = 5
Output : true

Input : arr[] = {1, 3, 5, 7, 8, 9}
        x = 6
Output : false
*/



const search = (arr, valueToSearch) => {
	let start = 0, end = arr.length-1;
	let mid;
	
	while(start <= end) {
		mid = Math.floor((start + end) / 2);
		console.log(arr[mid], valueToSearch)
		if (arr[mid] === valueToSearch) return true;
		else if (valueToSearch > arr[mid] )
			start = mid + 1
		else
			end = mid - 1
	}
	return false;
}

const length = 100000;
let x, found, now, number = 1;
const items = Array.from({length}, () => number++);

now = Date.now();
x = items[Math.floor(Math.random() * items.length)];
found = search(items, x);
console.log(`value to search ${x} found ${found}`)
console.log(`Execution time... ${Date.now() - now}ms`)

now = Date.now();
x = length + 1;
found = search(items, x);
console.log(`value to search ${x} found ${found}`)
console.log(`Execution time... ${Date.now() - now}ms`)

// Run script ➜ node binary.search.js
