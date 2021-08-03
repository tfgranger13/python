// singly linked lists
// ListNode class: we'll be using this

class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// var x = new ListNode(19);

// var y = new ListNode(7);
// x.next = y;

// var z = new ListNode(-257);
// y.next = z;

// var a = new ListNode(8);
// a.next = x;


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

function generateNewList(length, min_value, max_value) {
    var generated_sll = new SinglyLinkedList();
    for (let i = 0; i < length; i++) {
        generated_sll.addToFront(
            Math.round(Math.random() * (max_value - min_value) + min_value)
        );
    }
    return generated_sll;
}

// new_sll.addToBack(2);

// new_sll.addToFront(7);
// new_sll.addToFront(18);
// new_sll.addToFront(5);

// new_sll.addToBack(4);

// console.log(new_sll.display());

// console.log(new_sll.contains(5));
// console.log(new_sll.contains(9000));


// bonus: making these linked lists to test is kind of tedious. what if...
// what if... we had a function (not a method of the SLL class) to make them
// for us?
// generateNewList(length, min_value, max_value) -> creates a new SLL of the
// given length, with nodes containing values from min_value up to max_value
// some random integers may be helpful here
// generateNewList(5, 1, 10) -> 6 - 8 - 2 - 2 - 10, 1 - 9 - 4 - 3 - 6, etc.

function generateSLLFromArray(arr) {
    // create new singly linked list
    var generated_sll = new SinglyLinkedList();
    // for loop to iterate through input array
    for (let i = 0; i < arr.length; i++) {
        // add the value of the array to the list
        generated_sll.addToBack(arr[i]);
    }
    return generated_sll;
}

var test_list = generateSLLFromArray([9, 4, 7, 1, 5, 7, 9, 2, 8, 3]);
console.log(test_list.display());
test_list.partition(5);
console.log(test_list.display());

