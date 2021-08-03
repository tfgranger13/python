// binarySearch(input, target ... ?)
// given an input (a array of sorted integers) and a target value to search for
// return true if the value is found in the array and false otherwise
// we gotta do this recursively!
// you may need another two parameters
// this will have a big O time complexity of log n
// https://www.bigocheatsheet.com/
// don't look it up plz, ty :)

function binarySearch(input, target, lowerBound = 0, upperBound = input.length - 1) {
    if (input[Math.floor((lowerBound + upperBound)/2)]==target){
        return true;
    }
    else if (Math.abs(lowerBound - upperBound) == 1){
        if (input[Math.floor((lowerBound + upperBound)/2)]<target){
            var low = Math.floor((lowerBound + upperBound)/2);
        return binarySearch(input, target, lowerBound = upperBound, upperBound)
        }
        else if ((input[Math.floor((lowerBound + upperBound)/2)]>target)){
            var high = Math.floor((lowerBound + upperBound)/2);
            return binarySearch(input, target, lowerBound, upperBound = lowerBound)
        }
    }
    else if (input[Math.floor((lowerBound + upperBound)/2)]<target && (lowerBound != upperBound)){
        var low = Math.floor((lowerBound + upperBound)/2);
        return binarySearch(input, target, lowerBound = low, upperBound);
    }
    else if ((input[Math.floor((lowerBound + upperBound)/2)]>target) && (lowerBound != upperBound)){
        var high = Math.floor((lowerBound + upperBound)/2);
        return binarySearch(input, target, lowerBound, upperBound = high);
    }
    else return false
}

var test_list = [1, 2, 3, 5, 7, 8, 9, 10, 12, 13, 15, 16, 17]
// missing: 4, 6, 11, 14

console.log(binarySearch(test_list, -11)) // return false
console.log(binarySearch(test_list, 27)) // return false
console.log(binarySearch(test_list, 11)) // return false
console.log(binarySearch(test_list, 17)) // return true
console.log(binarySearch(test_list, 9)) // return true
console.log(binarySearch(test_list, 1)) // return true