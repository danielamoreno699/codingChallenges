class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

const head = new ListNode(3);
head.next = new ListNode(2);
head.next.next = new ListNode(0);
head.next.next.next = new ListNode(-4);

let current = head; // Start at the head node

while (current !== null) {
    console.log(current.val);

    current = current.next; // Move to the next node
}
