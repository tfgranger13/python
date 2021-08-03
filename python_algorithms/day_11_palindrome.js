class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }
    // addToFront - adds a node with the given value to the head of the list
    addToFront(value) {
        var new_node = new ListNode(value);

        // if nothing is in the list
        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    // addToBack - adds a node with the given value to the tail of the list
    addToBack(value) {
        var new_node = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }

    }
    // contains - returns true if target is in the linked list (as a node value),
    // false otherwise
    contains(target) {


        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }

        return false;
    }

    // display()
    // return a string with the value of every node from the
    // linked list, head to tail - like "3 - 7 - 13 - 4 - 8"
    display() {
        var output = '';

        var runner = this.head;

        if (runner == null) {
            return 'empty';
        }
        // while loop to run thru list
        while (runner.next != null) {
            output += runner.value + ' - ';
            runner = runner.next;
        }
        // add one more outside of the loop to account for the last value
        output += runner.value;

        return output;
    }


    // day 6 algo

    removeFront() {

        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // only one value
        else if (this.head == this.tail) {
            this.head = null;
            this.tail = null;
            return this.value;
        }

        // two or more values
        else {
            var oldHead = this.head;
            this.head = this.head.next;
            oldHead.next = null;
            return oldHead.value;
        }

    }

    // removeBack() - remove the tail of the linked list and return its value
    // again, this means this.tail will change
    // as above - is there a special case for linked lists with a minimal number of
    // nodes inside them?

    removeBack() {
        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // only one value
        else if (this.head == this.tail) {
            this.head = null;
            this.tail = null;
            return this.value;
        }

        // only two values
        else if (this.head.next == this.tail) {
            var temp = this.tail;
            this.head.next = null;
            this.tail = this.head;
            return temp.value;
        }

        // three or more values
        else {
            var runner = this.head;

            while (runner.next.next != null) {
                runner = runner.next;
            }

            this.tail = runner;
            runner.next = null;
            return runner.value;
        }

    }

    // findMinNode() - find the node in the linked list with the lowest value
    // and return that node - the node itself, not its value
    // if you find two or more nodes tied for that value,
    // return the first one you find. do not modify the linked list/contents
    // in any way - this is non-destructive.
    // (we want to use this code later - make sure it works well!)

    findMinNode() {
        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // one or more values
        else {
            // variable to hold lowest node, set to first value in the list
            var lowest_node = this.head;
            // create runner to iterate thru list
            var runner = this.head;
            // while loop to run thru list
            while (runner != null) {
                // if check to see if the value of the runner node is less than the value of the current lowest node
                if (runner.value < lowest_node.value) {
                    // if the value is lower, set lowest_node to be the current runner
                    lowest_node = runner
                }
                // increase runner
                runner = runner.next;
            }
            // check last value outside the while loop; unnecessary with modified while loop conditions
            // if (runner.value < lowest_node.value) {
            //     // if the value is lower, set lowest_node to be the current runner
            //     lowest_node = runner
            // }
            return lowest_node;
        }
    }

    // findMaxNode() - find the node in the linked list with the highest value
    // and return that node - the node itself, not its value
    // if you find two or more nodes tied for that value,
    // return the first one you find. do not modify the linked list/contents
    // in any way - this is non-destructive.
    // (again, we want to reuse this code later - make it good!)

    findMaxNode() {
        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // one or more values
        else {
            // variable to hold highest node, set to first value in the list
            var highest_node = this.head;
            // create runner to iterate thru list
            var runner = this.head;
            // while loop to run thru list
            while (runner != null) {
                // if check to see if the value of the runner node is less than the value of the current lowest node
                if (runner.value > highest_node.value) {
                    // if the value is lower, set lowest_node to be the current runner
                    highest_node = runner
                }
                // increase runner
                runner = runner.next;
            }
            // one more check for the last one at the end - not necessary changing while conditions
            // if (runner.value > highest_node.value) {
            //     // if the value is lower, set lowest_node to be the current runner
            //     highest_node = runner
            // }
            return highest_node;
        }
    }


    // Day 7 algos

    // moveMinToFront() - find the node with the smallest value in the linked
    // list (hmmmm) and make it the head of the list. note that the node itself
    // needs to be moved - you cannot just swap the values of the two nodes!
    // if your linked list looks like this:
    // 8 - 4 - 1 - 2 - 7
    // it should end up looking like this:
    // 1 - 8 - 4 - 2 - 7
    // what if the node is already at the head? what if the linked list is
    // small or empty? be careful!

    moveMinToFront() {
        var min = this.findMinNode();
        var runner = this.head;

        // if the had is min
        if (this.head == min) {
            return this;
        }
        else if (this.tail == min) {
            // while loop to find the node before min
            while (runner.next != min) {
                // if check to see if the value of the runner node is less than the value of the current lowest node
                runner = runner.next;
            }
            runner.next = min.next;
            this.tail = runner;
            // set min.next to current head
            min.next = this.head;
            // set min as new head
            this.head = min;
            return this;
        }
        else {
            // while loop to find the node before min
            while (runner != null) {
                // if check to see if the value of the runner node is less than the value of the current lowest node
                if (runner.next == min) {
                    // change runner.next to min.next
                    runner.next = min.next;
                }
                // increase runner
                runner = runner.next;
            }
            // set min.next to current head
            min.next = this.head;
            // set min as new head
            this.head = min;
            return this;
        }
    }

    // moveMaxToBack() - find the node with the largest value in the linked
    // list (...) and make it the tail of the list. 
    // if your linked list looks like this:
    // 1 - 8 - 4 - 2 - 7
    // it should end up looking like this:
    // 1 - 4 - 2 - 7 - 8
    // remember to check for edge cases

    moveMaxToBack() {
        // temp var for max value
        var max = this.findMaxNode();
        var runner = this.head;

        // if the max is the current tail or if only one value
        if (this.tail == max) {
            return this;
        }
        else if (this.head == max) {
            this.head = max.next;
            // set max.next to null
            max.next = null;
            // set tail.next to max
            this.tail.next = max;
            return this;
        }
        else {
            // while loop to find the node after max
            while (runner.next != max) {
                // if check to see if the value of the runner node is less than the value of the current lowest node
                if (runner.next == max) {
                    // change runner.next to min.next
                    runner.next = max.next;
                }
                // increase runner
                runner = runner.next;
            }
            // set max.next to null
            max.next = null;
            // set tail.next to max
            this.tail.next = max;
            return this;
        }
    }

    // remember that we can divide this into multiple problems
    // 1 - 8 - 4 - 2 - 7
    // 1 - 4 - 2 - 7

    // partition(target)
    // rearrange the nodes in the list so that all nodes with values less than
    // the target value come first in the list, then all nodes with the target
    // value, then all nodes with values greater than the target value
    // if there are no nodes with values greater or less than the target value,
    // or no nodes with the target value at all, the function should still work
    // if the target is 5, and the list is 8 - 7 - 1 - 5 - 4 - 5 - 2 - 8 - 3
    // the list should rearrange so that the nodes (represented by values)
    // are in this order:
    // 1 - 4 - 2 - 3 - 5 - 5 - 8 - 7 - 8
    // if the target 5, and the list contains:
    // 8 - 1 - 7 - 2 - 4 - 9 - 0 - 1 - 3 - 8
    // the output should be:
    // 1 - 2 - 4 - 0 - 1 - 3 - 8 - 7 - 9 - 8
    // order of nodes does not matter as long as the above rules 
    // for placement are respected
    // remember to fix your head and tail afterwards
    // remember that we cannot just swap node values
    // if you are iterating through the list using a runner and constantly moving
    // nodes to the end, you are likely to get stuck in a loop
    // bonus: can you do it without using an array(s)?
    // other bonus: can you do it without using an array -and- without using
    // another instance(s) of our SinglyLinkedList class?
    partition(target) {
        // while loop for runner
        // if runner is less than target, move to front
            // if it's not this.tail (create temp var to check)
                    // move to front
                    // add to runner
                // if it is this.tail
                    // move and then break loop
        // if runner is equal to target, leave it alone
            // if runner is this.tail
                // break
            // if not tail
                // add to runner
        // if runner is more than target
            // if it's not this.tail
                // move to back
                // add to runner
            // if it is this.tail
                // move and then break loop


        var final_tail = this.tail;
        var runner = this.head;
        var temp_new_head = null;
        var temp_new_tail = null;
        // while loop for runner
        while (runner != null) {
            console.log(runner.value);
            // if runner is less than target, move to front
            if (runner.value < target) {
                // if it's not this.tail (create temp var to check)
                if (runner != final_tail) {
                    // move to front
                    runner.next = this.head;

                    // add to runner
                    runner = runner.next;
                }
                    // if it is this.tail
                    else {
                        // move and then break loop
                        runner.next = this.head;
                        break;
                    }
            }
            // if runner is equal to target, leave it alone
            else if (runner.value == target) {
                // if runner is this.tail
                    // break
                // if not tail
                    // add to runner
                    runner = runner.next;
            }
            // if runner is more than target
            else {
                // if it's not this.tail
                    // move to back
                    // add to runner
                    runner = runner.next;
                // if it is this.tail
                    // move and then break loop
            }
        }
    }
}

class SLLStack {
    constructor() {
        this.head = null;
        this.tail = null;
        this.stack_size = 0;
    }
    // push(value) - adds the given value to the stack
    push(value) {

        // add_to_front
        var new_node = new ListNode(value);

        // if nothing is in the list
        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }

        this.stack_size ++;
    }


    // pop() - removes the top value from stack and returns it
    pop() {

        // remove front
        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // only one value
        else if (this.head == this.tail) {
            var return_value = this.head.value;
            this.head = null;
            this.tail = null;
            this.stack_size --;
            return return_value;
        }

        // two or more values
        else {
            var oldHead = this.head;
            this.head = this.head.next;
            oldHead.next = null;
            this.stack_size --;
            return oldHead.value;
        }
    }

    // top() - returns the top value without removing it
    top() {
        // // return the value of the tail
        // return this.tail.value

        // return the value of the head
        return this.head.value;
    }

    // contains(target) - returns true if the target value is in the stack,
    // false if not
    contains(target) {

        // same as contains()
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }

        return false;
    }

    // isEmpty() - returns true if the stack is empty, false otherwise
    isEmpty() {
        return (this.head == null && this.tail == null)
    }

    // size() - returns the size of the stack

    size() {
        return this.stack_size;
    }
}

class SLLQueue {
    constructor() {
        this.head = null;
        this.tail = null;
        this.queue_size = 0;
    }

    // enqueue(value) - adds the given value to the queue (at the tail)
    enqueue(value) {

        // add to back
        var new_node = new ListNode(value);

        if (this.head == null && this.tail == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
        this.queue_size++;
    }

    // dequeue() - removes the top value from queue and returns it
    dequeue() {

        // remove from front
        // empty list
        if (this.head == null && this.tail == null) {
            return undefined;
        }

        // only one value
        else if (this.head == this.tail) {
            this.head = null;
            this.tail = null;
            this.queue_size--;
            return this.value;
        }

        // two or more values
        else {
            var oldHead = this.head;
            this.head = this.head.next;
            oldHead.next = null;
            this.queue_size--;
            return oldHead.value;
        }
    }

    // front() - returns the top value without removing it
    front() {
        return this.head.value;
    }

    // contains(target) - returns true if the target value is in the queue,
    // false if not
    contains(target) {
        // same as contains()
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }

        return false;
    }

    // isEmpty() - returns true if the queue is empty, false otherwise
    isEmpty() {
        return (this.queue_size == 0)
    }

    // size() - returns the size of the queue
    size() {
        return this.queue_size;
    }

    // method: compareQueues
    // return true if the queues have the same values in the same order
    // false otherwise
    // important: this is a non-destructive operation!
    // do not modify either queue
    compareQueues(other_queue) {
        var og_runner = this.head;
        var other_runner = other_queue.head;

        if (this.queue_size != other_queue.queue_size) {
            return false;
        }

        else {
            while (og_runner != null) {
                if (og_runner.value != other_runner.value) {
                    return false;
                }
                og_runner = og_runner.next;
                other_runner = other_runner.next;
            }
        }
        return true;
    }

    // isPalindrome() - return true if the values of the queue form a palindrome,
    // and false otherwise. essentially, if the queue were read tail to head
    // instead of head to tail, would we get the same results?
    // don't put the values of the queue into an array!
    // (or turn them into a string, either - your queue listnode values
    // may not always be able to be turned into a string)
    // do not modify the queue state in any way
    // also don't add some kind of tricky extra queue methods - they're not needed
    // maybe... use a stack? you'll need to copy that class into this file
    // you ain't gotta tho nbd it's just a suggestion

    isPalindrome() {
        // make a runner
        // iterate thru the list to make a stack
        // compare the queue with the stack values to see if they are the same value
        // return false if not
        // else return true

        // make the runner, establish the stack
        var q_runner = this.head;
        var stack = new SLLStack();

        // adding the values to the stack
        while (q_runner != null){
            stack.push(q_runner.value);
            q_runner = q_runner.next;
        }

        var stack_runner = stack.head;
        while (stack_runner != null){
            stack_runner = stack_runner.next;
        }

        // reset runner, iterate thru again to compare with popping from the stack
        q_runner = this.head;
        while (q_runner != null){
            var stack_pop = stack.pop()
            if (q_runner.value != stack_pop){
                return false;
            }
            q_runner = q_runner.next;
        }
        return true;
    }
}

var x = new SLLQueue();

console.log(x.isPalindrome());