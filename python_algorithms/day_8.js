class ArrayStack {
    constructor() {
        this.contents = [];
    }

    // push(value) - adds the given value to the stack
    push(value) {
        this.contents.push(value);
    }

    // pop() - removes the top value from stack and returns it
    pop() {
        this.contents.pop();
    }
    
    // top() - returns the top value without removing it
    top() {
        return this.contents[this.contents.length-1];
    }

    // contains(target) - returns true if the target value is in the stack,
    // false if not
    contains(target) {
        // for loop to go through the array
        for (let i = 0; i < this.contents.length; i++) {
            // check if the value is equal to the target
            if (this.contents[i] == target){
                return true;
            }
        }
            return false;
    }

    // isEmpty() - returns true if the stack is empty, false otherwise
    isEmpty() {
        // check if the array had no length
        if (this.contents.length == 0){
            return true;
        }
        else {
            return false;
        }
    }

    // size() - returns the size of the stack
    size() {
        return this.contents.length;
    }
}

// make sure you test all six methods!
// make sure that you test any edge cases you find using these methods as well

var x = new ArrayStack();

x.push(5);
console.log(x);
x.push(7);
x.push(19);
console.log(x);
console.log(x.size());
x.pop();
console.log(x);
console.log(x.top());
console.log(x.size());
x.push(13);
x.push(23);
console.log(x);
console.log(x.contains(13));
console.log(x.contains(100));
console.log(x.isEmpty());
x.pop();
x.pop();
x.pop();
x.pop();
console.log(x);
console.log(x.isEmpty());