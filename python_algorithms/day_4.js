// bookIndex(input)
// input is an array of integers (in order) representing pages in a book
// where a given term is found, and the output is a string suitable
// for printing in a book's index
// if the input is [58, 104, 105, 106, 192, 194, 195, 196]
// the output is: "58, 104-106, 192, 194-196"
// if the input is [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]
// the output is: "1-5, 8-12, 15, 17-18"

// suggestion: break this into two parts, or maybe even two
// functions - get your array of integers and turn it into an array
// of strings, then turn that array of strings into a single string
// [58, 104, 105, 106, 192, 194, 195, 196]
// ["58", "104-106", "192", "194-196"]
// "58, 104-106, 192, 194-196"

// does not handle:
// [ix, x, xi, 1, 2, 3, 7, 8, 9, 32a, 47b, 48b]
// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point

        // array.join(', ') to combine the elements of the array

function bookIndex(input) {

    // output is empty array to hold ranges
    var output = ""
    // set the first input as temp_open and temp_close
    var temp_open = input[0]
    var temp_close = input[0]

    // for loop (from 1 to end) to check the next values
    for (let i = 1; i < input.length; i++) {

        // if input[i] == temp_close + 1
        if (input[i] == temp_close + 1) {
            // store i as temp_close
            var temp_close = input[i];
        }

        // else if the next number is not equal to the previious value + 1
        else if (input[i] != temp_close + 1) {

            // if temp_open is the same as temp_close
            if (temp_open == temp_close) {
                // add to string "temp_open, "
                output += `${temp_open}, `
                temp_open = input[i];
                temp_close = input[i];
            }

            // else if temp_open is NOT the same as temp_close
            else if (temp_open != temp_close) {
                // add to string "temp_open - temp_close, "
                output += `${temp_open}-${temp_close}, `
                // set new value to temp_open and temp_close
                // input[i] = temp_open;
                // input[i] = temp_close;
                temp_open = input[i];
                temp_close = input[i];
            }
        }
    }
    // add the final output to the output
    if (temp_open == temp_close) {
        // add to string "temp_open, "
        output += `${temp_open}`
    }
    else if (temp_open != temp_close) {
        // add to string "temp_open - temp_close, "
        output += `${temp_open}-${temp_close}`
    }
    // return the output
    return output;
}

console.log(bookIndex([58, 104, 105, 106, 107, 192, 194, 195, 201]));
console.log(bookIndex([1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]));