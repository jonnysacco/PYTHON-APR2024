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
    // YOU CODE HERE
    let start = 0
    let end = str.length - 1
    while(start < end){
      if(str[start] === str[end]){
        start++
        end --
      } else {
        return false
      }
    }
    return true
  }
  
  function isPalindrome2(str) {
    var reverseString = str.split("").reverse().join("");
    return (reverseString === str)
    // .split("") --> turn to an array
    // .reverse() --> reverse an array
    // .join("") --> join an array into a string
  } 
  
  /*  
    Longest Palindrome
  
    For this challenge, we will look not only at the entire string provided,
    but also at the substrings within it.
    Return the longest palindromic substring. 
  
    Strings longer or shorter than complete words are OK.
  
    All the substrings of "abc" are:
    a, ab, abc, b, bc, c
  */
  
  const str5 = "what up, daddy-o?";
  const expected5 = "dad";
  
  const str6 = "uh, not much";
  const expected6 = "u";
  
  const str7 = "Yikes! my favorite racecar erupted!";
  const expected7 = "e racecar e";
  
  const str8 = "a1001x20002y5677765z";
  const expected8 = "5677765";
  
  const str9 = "a1001x20002y567765z";
  const expected9 = "567765";
  
  /**
   * Finds the longest palindromic substring in the given string.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str
   * @returns {string} The longest palindromic substring from the given string.
   */
  
  function longestPalindromicSubstring(str) {
    let longest = "";
  
    for (let i = 0; i < str.length; i++) {
      for (let j = i; j < str.length; j++) {
        let substring = str.slice(i, j + 1);
        let isPalindrome = true;
  
        for (let k = 0; k < substring.length / 2; k++) {
          if (substring[k] !== substring[substring.length - 1 - k]) {
            isPalindrome = false;
            break;
          }
        }
  
        if (isPalindrome && substring.length > longest.length) {
          longest = substring;
        }
      }
    }
    return longest;
  }
  
  function longestPalindromicSubstring(str = "") {
    let longestPalindrome = str[0];
  
    // generate every sub string 1 at a time and check
    // if it is a palindrome and how long it is.
    for (let i = 0; i < str.length; i++) {
      for (let j = i + 1; j < str.length + 1; j++) {
        let subStr = str.slice(i, j);
  
        // No need to check if it is a palindrome if it can't be longer.
        if (subStr.length > longestPalindrome.length && isPalindrome(subStr)) {
          longestPalindrome = subStr;
        }
      }
    }
    return longestPalindrome;
  }
  
  /**
   * - Time: O(n^2) quadratic.
   * - Space: O(n) linear.
   */
  function longestPalindromicSubstring2(str = "") {
    let longestPal = "";
    const midIdx = Math.floor(str.length / 2);
  
    for (let i = 0; i < str.length; i++) {
      /* 
      Once we pass the center, the longest possible pal from there gets shorter
      because we will hit the right end of the string sooner so we can early exit
      if there aren't enough chars left.
      */
      if (i > midIdx && str.length - 1 < longestPal.length) {
        break;
      }
  
      const oddPalindrome = concatPalindromeFromCenter(str, i, i);
      const evenPalindrome = concatPalindromeFromCenter(str, i, i + 1);
  
      if (oddPalindrome.length > longestPal.length) {
        longestPal = oddPalindrome;
      }
  
      if (evenPalindrome.length > longestPal.length) {
        longestPal = evenPalindrome;
      }
    }
    return longestPal;
  }
  
  /**
   * Finds the longest palindrome by expanding out from the given indexes.
   * - Time: O(n) linear. n = right - left which could be the full string.
   * - Space: O(n) linear.
   * @param {string} str
   * @param {number} left Left index to expand out from.
   * @param {number} right Right index to expand out from.
   * @returns {string} The longest palindrome from the starting given indexes.
   */
  function concatPalindromeFromCenter(str = "", left = 0, right = 0) {
    let leftPalSub = "";
    let rightPalSub = "";
  
    // Used for checking odd palindrome.
    if (left === right) {
      rightPalSub = str[right];
      left--;
      right++;
    }
  
    while (left >= 0 && right < str.length && str[left] === str[right]) {
      leftPalSub = str[left] + leftPalSub; // prepend.
      rightPalSub += str[right];
      left--;
      right++;
    }
    return leftPalSub + rightPalSub;
  }