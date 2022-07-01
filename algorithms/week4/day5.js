/*
Sum To One Digit
Implement a function sumToOne(num)​ that,
given a number, sums that number’s digits
repeatedly until the sum is only one digit. Return
that final one digit result.
Tips:
    to access digits from a number, need to convert it .toString() to access each digit via index
    parseInt(arg) returns arg parsed as an integer, or NaN if it couldn't be converted to an int
    isNaN(arg) used to check if something is NaN
*/

const num1 = 5;
const expected1 = 5;

const num2 = 10;
const expected2 = 1;

const num3 = 25;
const expected3 = 7;

/**
 * Sums the given number's digits until the number becomes one digit.
 * @param {number} num The number to sum to one digit.
 * @returns {number} One digit.
 */
function sumToOneDigit(num) {
    num = Math.floor(num)

    if (num > 9) {
        let newnumber = 0;

        newnums = Array.from(num.toString()).map(Number);
        for (let i = 0; i < newnums.length; i++) {
            newnumber += newnums[i];
        }

        if (newnumber > 9) {
            return sumToOneDigit(newnumber);
        }
        else {
            return newnumber;
        }

    }
    else {
        return num;
    }
}

console.log(sumToOneDigit(num1));
console.log(sumToOneDigit(num2));
console.log(sumToOneDigit(num3));

// http://algorithms.dojo.news/static/Algorithms/index.html#LinkTarget_2129
/* 
String Anagrams
Given a string,
return array where each element is a string representing a different anagram (a different sequence of the letters in that string).
Ok to use built in methods
*/

const str1 = "lim";
// const expected1 = ["ilm", "iml", "lim", "lmi", "mil", "mli"];
// Order of the output array does not matter

/**
 * Add params if needed for recursion.
 * Generates all anagrams of the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {Array<string>} All anagrams of the given str.
 */
function generateAnagrams(str) {
    if (str.length < 2){
        return str;
    }
    var array = []
    for (var i = 0; i<str.length;i++){
        var beg = str[i];
        var left_side = str.substring(0, i) + str.substring(i+1);
        var inside = generateAnagrams(left_side);
        for (var j = 0; j < inside.length; j++){
            array.push(beg + inside[j]);
        }
    }
    return array
}

console.log(generateAnagrams(str1))

