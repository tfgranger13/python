// reverseString(input)
// input is a string, output is string but backwards
// empty string revered is empty
// single letter is the same letter

// index string like an array


// another method of creating functions:
// reverseString = (input) => {}

function reverseString(input){
    // create a new empty string variable for the output
    var reversed = "";
    // create a for loop for the length of the string starting backwards
    for (var i = input.length - 1; i >=0; i--) {
        // add that letter to the output
        reversed += input[i];
    }

    // return the output
    console.log(reversed);
    return reversed;
}

reverseString("Hello World!");