// inOrderCombinations(input, ...? output)
// input is a string
// return an array with all strings you could make with the characters from the
// given input, in the order that they're presented (i.e. the order they appear in
// the input)
// (output array order doesn't matter)
// "abc" -> ["", "c", "b", "bc", "a", "ac", "ab", "abc"] (8)
// "zhk" -> ["", "z", "h", "k", "hk", "zh", "zk", "zhk"] (8)
// "hjj" -> ["", "h", "j", "j", "hj", "hj", "jj", "hjj"]
// "tkps" -> ["", "t", "k", "p", "s", "tk", "tp", "ts", "kp", "ks", "ps",
// "tkp", "tks", "tps", "kps", "tkps"] (16)
// make sure to use recursion (probably going to call it twice)
// input of length n leads to 2^n output elements
// every character in the output appears with equal occurance
// test with at least 4 characters in input, no more than 6
// new note: no need to check contents of output


function inOrderCombinations(input, output = [], position = 0, partial = '') {
    // remember that you may need some more parameters above

    if (position == input.length) {
        output.push(partial);
    }

    else {
        inOrderCombinations(input, output, position + 1, partial + input[position]);
        inOrderCombinations(input, output, position + 1, partial);
    }

    return output;
}

var result = inOrderCombinations('zqh');

// console.log(result);
// console.log(result.length);

function inOrderSubsets(str, solutions = [], partial = "") {
    solutions.push(partial);

    for (let i = 0; i < str.length; i++) {
        const sliced = str.slice(i + 1);
        console.log(`sliced: ${sliced}, partial: ${partial}, str[i]: ${str[i]}`)
        inOrderSubsets(sliced, solutions, partial + str[i]);
    }

    return solutions;
}

var result = inOrderSubsets('zqh');

function recursive_countdown(input, output = []) {
    output.push(input)
    if (input - 1 >= 0) {
        recursive_countdown(input - 1, output)
    }
    return output;
}

// console.log(recursive_countdown(5));

// inOrderCombinations(input, ...? output)
// input is a string
// return an array with all strings you could make with the characters from the
// given input, in the order that they're presented (i.e. the order they appear in
// the input)
// (output array order doesn't matter)
// "abc" -> ["", "c", "b", "bc", "a", "ac", "ab", "abc"] (8)
// "zhk" -> ["", "z", "h", "k", "hk", "zh", "zk", "zhk"] (8)
// "hjj" -> ["", "h", "j", "j", "hj", "hj", "jj", "hjj"]
// "tkps" -> ["", "t", "k", "p", "s", "tk", "tp", "ts", "kp", "ks", "ps",
// "tkp", "tks", "tps", "kps", "tkps"] (16)
// make sure to use recursion (probably going to call it twice)
// input of length n leads to 2^n output elements
// every character in the output appears with equal occurance
// test with at least 4 characters in input, no more than 6


function inOrderCombinations(input, output = [], counter = 0, position = 0) {
    // counter to keep track of how many letters are added to the output at this iteration
    // increase counter when recursively calling the function

    // position to keep track of what letter we are starting at
    // increase position when recursively calling the function

    // nested while loops? iterate through counter first, then position for each counter

    while (counter <= input.length) {
        console.log(`counter is at ${counter}`)
        // TODO: figure out why this gets stuck at position = 4
        while (position <= input.length - 2) {
            console.log(`position is at ${position}`)
            for (let j = position; j <= input.length - 1; j++) {
                var temp = [];
                console.log(`adding ${input[position]} to the temp`)
                temp.push(input[position])
                for (let i = position + 1; i <= counter; i++) {
                    console.log(`adding ${input[i]} to the temp`)
                    temp.push(input[i])
                }
                // TODO: need to condense temp into one element to add just the one string to the output
                console.log(`adding ${temp} to the output`)
                output.push(temp);
            }
        }
        inOrderCombinations(input, output, counter, position + 1)
    }
    inOrderCombinations(input, output, counter + 1, position)

    return output;
}

console.log(inOrderCombinations(input = 'abcd', output = [], counter = 0, position = 0));