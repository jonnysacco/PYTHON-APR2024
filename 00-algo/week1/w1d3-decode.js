/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
            
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {}



function decodeStr1(str) {
    let tempNum = "";
    let current = "";
    let result = "";
    for (let i = 0; i < str.length; i++) {
        if (isNaN(str[i])) { // if it is a letter
            if (tempNum) {
                tempNum = parseInt(tempNum) // Change it to a number
                while(tempNum > 0){
                    result += current
                    tempNum--
                }
                tempNum = "";
            }
            current = str[i];
        }
        else { // if it is a number
            tempNum += str[i];
        }
    }
    if (tempNum) {
        result += current.repeat(+tempNum);
    }
    return result;
  }


function decodeStr2(str) {
  let tempNum = "";
  let current = "";
  let result = "";
  for (let i = 0; i < str.length; i++) {
      if (isNaN(str[i])) { // if it is a letter
          if (tempNum) {
              result += current.repeat(+tempNum);
              tempNum = "";
          }
          current = str[i];
      }
      else { // if it is a number
          tempNum += str[i];
      }
  }
  if (tempNum) {
      result += current.repeat(+tempNum);
  }
  return result;
}