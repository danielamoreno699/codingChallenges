
const mergeTwoLists = function(l1, l2) {
    let dummy = new ListNode(0);
    let head = dummy;
    while(l1 && l2) {
        if(l1.val < l2.val) {
            dummy.next = l1;
            l1 = l1.next;
        } else {
            dummy.next = l2;
            l2 = l2.next;
        }
        dummy = dummy.next;
    }
    if(l1) {
        dummy.next = l1;
    }
    if(l2) {
        dummy.next = l2;
    }
    return head.next;
}