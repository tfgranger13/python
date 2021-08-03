function sigma(n){
    
    if (n==1){
        return n;
    }

    return n + sigma(n-1);

}

// console.log(sigma(10));


function factorial(n){

    if (n==1){
        return n;
    }
    return n * factorial(n-1);

}

// console.log(factorial(5));

function fibonacci(n){
    
    if (n<=1){
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2)

}

console.log(fibonacci(7));


// console.log(fibonacci(100));


// memoization
function fib(n, results = {}){
    if (n<=1){
        return n;
    }
    if (results[n]!= undefined){
        return results[n];
    }

    result = fib(n-1, results) + fib(n-2, results)

    results[n] = result

    return result
}

console.log(fib(100))