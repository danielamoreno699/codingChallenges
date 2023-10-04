let head = [3,2,0,-4]

let current = head; // Start at the head node
current.next = head.next;

while (current !== null) {
    

    current = current.next; // Move to the next node
}

if (current.next == null && current.next.next != null){
   return true
}

class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

function hasCycle(head) {
    let pointer = head; // Start at the head node

    while (pointer !== null && pointer.next !== null) {
        pointer = pointer.next.next; // Move the pointer two steps

        if (pointer === head) {
            // Cycle detected
            return true;
        }

        head = head.next; // Move the head one step

    }

    // No cycle found
    return false;
}