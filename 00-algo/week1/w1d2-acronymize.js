/* 
  Acronyms

  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 

  Do it with .split first if you need to, then try to do it without
*/

const str1 = "object oriented programming";
const expected1 = "OOP";

// The 4 pillars of OOP
const str2 = "abstraction polymorphism inheritance encapsulation";
const expected2 = "APIE";

const str3 = "software development life cycle";
const expected3 = "SDLC";

// Bonus: ignore extra spaces
const str4 = "  global   information tracker    ";
const expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} wordsStr A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str){}


function acronymize3(str) {
  let acro = '';
  let split = str.split(" ");
  for (let i = 0; i < split.length; i++) {
      let word = split[i];
      if (word.length > 0) {
          acro += word[0].toUpperCase();
      }
  }
  return acro;
}

function acronymize1(str) {
  let returnStr = "";
  let arr = str.trim().split(" ");
  for(var i=0;i<arr.length;i++){
      if(arr[i] != ""){
          returnStr += arr[i][0];
      }
  }
  return returnStr.toUpperCase()
}

function acronymize2(str) {
  let trimStr = str.trim();
  let splitStr = trimStr.split(" ");
  console.log(splitStr)
  let acronym = "";
  for( let i=0; i < splitStr.length; i++){
      if( splitStr[i] === ""){
          continue
      }
      else{
          acronym += splitStr[i][0]
      }
  };
  acronym = acronym.toUpperCase();
  return acronym;

}



