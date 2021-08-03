// parensValid(input)
// input is a string
// return true if the input has a valid configuration of parentheses and false
// otherwise. by "return true/false" I mean the boolean value, not a string
// what's valid?
// - no more open parens than close parens or vice versa
// - no close parens that appear before a valid open paren
// - ignore all other characters that are not ( and )
// - () -> true
// - )( -> false
// - hello! -> true (???)
// - (()) -> true
// - (q(a)(x)(!(7(xx)(34)(2, 7, 11)))) -> true
// - (() -> false
// - hello!() -> true
// suggestion - don't bother trying to split the string...
// it won't do us any good and just makes things more complicated
// suggestion again - do we have to check every single character in the input?
// hypothetical input: ) followed by one billion characters
// or: a) followed by one billion characters
// or: a37()) followed by one billion characters

function parensValid(input) {
    // output = input.includes("(")
    openParen = 0;
    closingParen = 0;
    for (let i = 0; i < input.length; i++) {
        if (input[i] == "(") {
            openParen++;
        }
        else if (input[i] == ")" && openParen > closingParen) {
            closingParen++;
        }
        else if (input[i] == ")" && openParen <= closingParen) {
            return false;
        }
    }
    if (openParen != closingParen) {
        return false;
    }
    else{
        return true;
    }
}

// console.log(parensValid('()'));
// console.log(parensValid('(())'));
// console.log(parensValid('(q(a)(x)(!(7(xx)(34)(2, 7, 11))))'));
// console.log(parensValid(')('));
// console.log(parensValid('(()'));
// console.log(parensValid('hello!'));
// make your own test cases too!

// bracesValid(input)
// as above, but for parentheses, curly brackets (or curly braces) and square
// brackets - with the caveat that we can't have two sets of braces
// interleaved, or our function should return false, as follows:
// ([)] -> false
// the parentheses close before the square brackets do, which is Bad
// ()[]{} -> true
// (] -> false
// x(37[q{3, 7, 9}{22, 6, 91}])(32q) -> true
// ()]... -> false

function bracesValid(input) {
    // set counters for the characters we are looking for
    var openParen = 0;
    var closeParen = 0;
    var openBracket = 0;
    var closeBracket = 0;
    var openCurly = 0;
    var closeCurly = 0;
    // create an array to hold the closers we need to see
    // referred to as a stack
    var currentCloser = [];
    // loop through the input
    for (let i = 0; i < input.length; i++) {

        // if "(" is the first grouping symbol we see, add to the count and add to current closer array
        if (input[i]=="(") {
            openParen++;
            currentCloser.push(")");
        }
        // if ")" and we expect to see one (there's a "(" before it, it's the current closer)
        else if (input[i] == ")" && openParen > closeParen && currentCloser[currentCloser.length-1] == ")") {
            // add to closing parentheses counter
            closeParen++;
            // the grouping symbols are closed, so remove it from the closing symbols array
            currentCloser.pop();
        }
        // if ")" and we don't expect to see it (no "(" before it, it's not the current closer)
        else if (input[i] == ")" && (openParen <= closeParen || currentCloser[currentCloser.length-1] != ")")) {
            // the grouping symbols are incorrect, return false
            return false;
        }

        // repeat the above steps for "{"
        if (input[i]=="{") {
            openCurly++;
            currentCloser.push("}");
        }
        else if (input[i] == "}" && openCurly > closeCurly && currentCloser[currentCloser.length-1] == "}") {
            closeCurly++;
            currentCloser.pop();
        }
        else if (input[i] == "}" && (openCurly <= closeCurly || currentCloser[currentCloser.length-1] != "}")) {
            return false;
        }

        // repeat the above steps for "["
        if (input[i]=="[") {
            openBracket++;
            currentCloser.push("]");
        }
        else if (input[i] == "]" && openParen > closeBracket && currentCloser[currentCloser.length-1] == "]") {
            closeBracket++;
            currentCloser.pop();
        }
        else if (input[i] == "]" && (openParen <= closeBracket || currentCloser[currentCloser.length-1] != "]")) {
            return false;
        }
    }
    return true;
}

console.log(bracesValid("x(37[q{3, 7, 9}{22, 6, 91}])(32q)"));

// bonus: what if we also want to check angle brackets (< and >)? what if
// sometimes we care about curly braces but sometimes we don't?