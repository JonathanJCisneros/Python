// /* 
// Given a string,
// return a new string with the duplicates excluded
// Bonus: Keep only the last instance of each character.
// */

// const str1 = "abcABC";
// const expected1 = "abcABC";

// const str2 = "helloo";
// const expected2 = "helo";

// const str3 = "";
// const expected3 = "";

// const str4 = "aaaaa";
// const expected4 = "a";

// const str5 = "banana";
// const expected5 = "ban";

// /**
//  * De-dupes the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str A string that may contain duplicates.
//  * @returns {string} The given string with any duplicate characters removed.
//  */
function stringDedupe(str) {
    var newdict = {};
    var newstring = "";
    var curchar = "";

    for(var i = 0; i < str.length; i++){
        curchar = str[i];
        if(curchar in newdict) {
            continue;
        }
        else {
            newdict[curchar] = 1;
            newstring += curchar;
        }
    }
    return newstring;
}


console.log(stringDedupe(str1));

/* 
Given a string containing space separated words
Reverse each word in the string.
If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    return str.split(" ").map(word => word.split("").reverse().join("")).join(" ");
}

console.log(reverseWords(str2));
