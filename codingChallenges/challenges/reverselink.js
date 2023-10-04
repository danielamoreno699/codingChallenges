if( head ==null || head.next == null){
    return head 
}

let reverseList = reverseList(head.next);
head.next.next = head;
head.next = null;

return reverseList;