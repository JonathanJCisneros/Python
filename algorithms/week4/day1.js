/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const num1 = 5;
const expected1 = 15;
// Explanation: (1+2+3+4+5)

const num2 = 2.5;
const expected2 = 3;
// Explanation: (1+2)

const num3 = -1;
const expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) { 
    if (nums.length === 0) {
        return 0;
    }
    if (nums.length === 1) {
        return nums.pop();
    } else {
        return nums.pop() + sumArr(nums);
    }

}



/* 
Recursively sum an arr of ints
*/

const twoNums1 = [1, 2, 3];
const twoExpected1 = 6;

const twoNums2 = [1];
const twoExpected2 = 1;

const twoNums3 = [];
const twoExpected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums) { 
    
}