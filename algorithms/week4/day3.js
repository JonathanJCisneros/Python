/*
Recursive Binary Search
Input: SORTED array of ints, int value
Output: bool representing if value is found
Recursively search to find if the value exists, do not loop over every element.
Approach:
Take the middle item and compare it to the given value.
Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
function binarySearch(sortedNums, searchNum) {
    let middleNum =  Math.floor( sortedNums.length / 2 );
    let middleElement = sortedNums[middleNum];
    if (middleElement === searchNum ){
        return true;
    }
    else if ( middleElement < searchNum && sortedNums.length > 1 ) {
        return binarySearch( sortedNums.slice( 0, middleNum ), searchNum );
    }
    else if ( middleElement > searchNum && sortedNums.length > 1) {
        return binarySearch( sortedNums.slice( 0, middleNum ), searchNum );
    }
    else return false;
}

/* 
Recursively reverse a string
helpful methods:
str.slice(beginIndex[, endIndex])
returns a new string from beginIndex to endIndex exclusive
*/

const twoStr1 = "abc";
const twoExpected1 = "cba";

const twoStr2 = "";
const twoExpected2 = "";

/**
 * Recursively reverses a string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given str reversed.
 */
function reverseStr(str) {
    if(str.length <= 1) return str;
    else{
        return str[str.length -1] + reverseStr(str.substring(0,str.length-1));
    } 
}