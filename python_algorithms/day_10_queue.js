class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// a queue! first in, first out
// where should we add items? where are they removed from

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
}

// var x = new SLLQueue();

// x.enqueue(6);
// x.enqueue(8);
// x.enqueue(14);
// x.enqueue(23);
// console.log(x.size());
// console.log(x.contains(14));
// console.log(x.contains(329));
// console.log(x.front());
// console.log(x.dequeue());
// console.log(x.size());
// console.log(x.isEmpty());

// var y = new SLLQueue();
// y.enqueue(6);
// y.enqueue(8);
// y.enqueue(14);
// console.log(y.size());
// console.log(y.contains(14));
// console.log(y.contains(329));
// console.log(y.front());
// console.log(y.dequeue());
// console.log(y.size());
// console.log(y.isEmpty());


var a = new SLLQueue();
var b = new SLLQueue();
var c = new SLLQueue();
c.enqueue(13);


console.log(a.compareQueues(c));