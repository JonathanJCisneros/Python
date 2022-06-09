/* 
String: Is Palindrome
Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud"; 
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
   * Determines if the given str is a palindrome (same forwards and backwards).
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {boolean} Whether the given str is a palindrome or not.
   */
function isPalindrome(str) {
    var start = 0;
    var end = str.length-1;

    while (start < end) {
        if (str[start] === str[end]){
        }
        else{
            return false;
        }
        start++
        end--
    } 
    return true;
}

console.log(isPalindrome(str1))

/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

// const nums1 = [1, 13, 14, 15, 37, 38, 70];
// const expected1 = "1, 13-15, 37-38, 70";

// const nums2 = [5, 6, 7, 8, 9];
// const expected2 = "5-9";

// const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
// const expected3 = "1-3, 7, 9, 15-17";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {
    var temp = []
    for (i = 0; i < nums.length; i ++) {
        if (nums[i]+1 == nums[i + 1]) {
            var start = nums[i];
            while (nums[i]+1 == nums[i + 1]) {
                i ++;
            }
        var end = nums[i];
        temp.push(start + "-" + end);
        }
        else {
            temp.push(nums[i]);
        }
    }
    var newstring = temp.join(',');
    return newstring
}
