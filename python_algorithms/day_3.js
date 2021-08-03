function generateCoinChange(input) {
    // divide input and round down to see how many quarters you can use
    var quarters = Math.floor(input / 25);
    // use modulo to see what the remainder is
    var remainder = input % 25;

    // divide the remainder by 10 to see how many dimes you can use
    var dimes = Math.floor(remainder / 10);
    // use modulo to see what the remainder is
    var remainder = remainder % 10;

    // divide the remainder by 5 to see how many nickels you can use
    var nickels = Math.floor(remainder / 5);
    // use modulo to see what the remainder is
    var remainder = remainder % 5;

    // pennies are all that's left over
    var pennies = remainder;

    // print the result
    return `There are ${quarters} quarters, ${dimes} dimes, ${nickels} nickels, and ${pennies} pennies.`
}

// console.log(generateCoinChange(85))

function generateCoinChangeWithGivenValues(input, values) {

    // output is blank array to hold all the values of coins (unknown number of coins)
    // var output = []

        // output is an object
        // var output = {};

    // divide input by the value of the first currency, push it to the output array
    output.push(values[0][0], Math.floor(input / values[0][1]));
    // use modulo to see what the remainder is
    var remainder = input % values[0][1];

    for (let i = 1; i < values.length; i++) {
        // divide the remainder by next VALUE to see how many COIN_NAME you can use
        output.push(values[i][0], Math.floor(remainder / values[i][1]));

            // output[values[i][0], Math.floor(remainder / values[i][1])]

        // use modulo to see what the remainder is
        var remainder = remainder % values[i][1];
    }

    // bonus: what would you do if we couldn't guarantee a denomination of 1 being present? there are a few different answers, none of them inherently right
    // The correct answer is "Office Space"
    if (remainder != 0){
        var ourBankAccount = remainder;
        remainder = 0;
    }
    // print the result
    return output
}

console.log(generateCoinChangeWithGivenValues(52, [['copper', 12], ['silver', 8], ['gold', 3], ['plat', 1]]));
console.log(generateCoinChangeWithGivenValues(287854798585828040538, [['bitcoin', 32589], ['etherium', 2100], ['Bitcoin Cash', 490], ['Litecoin', 160], ['ripple', 2], ['Dogecoin', 1]]));