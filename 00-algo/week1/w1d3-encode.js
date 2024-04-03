/* 
  Given in an alumni interview in 2021.

  String Encode

  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";

  const str5 = "bbccddd";
  const expected5 = "b2c2d3";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
  function encodeStr(str) {}




function encodeStr(str) {

    counter = 1
    holderString = ""
    for(var i = 0; i < str.length; i++){
        holderString += str[i]
        while(str[i] === str[i+1]){
            counter ++
            i++
        }
        holderString += String(counter)
        counter = 1
    }
    if (str.length <= holderString.length){
        return str
    }
    else {
        str = holderString
        return str
    }
}