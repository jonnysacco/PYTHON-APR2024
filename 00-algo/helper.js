// String

message = "   Hello World"
console.log(message[10])

// To return the string/character in upper case
console.log(message.toUpperCase())

// To remove space in front / at the end
console.log(message.trim())

// To seprate a sentence into different elements and store in the array
sentence = "Morning Ninjas! Welcome to the class"
wordList = sentence.split(" ")
console.log(wordList)

str = "1hello"
// isNaN(var) --> is Not a number
console.log(isNaN(str[0])) // str[0]: 1 :  is a number
console.log(isNaN(str[1])) // str[1]: h : is Not a number