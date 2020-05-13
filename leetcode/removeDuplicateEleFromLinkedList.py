'''83. Remove Duplicates from Sorted List
Easy

1321

103

Add to List

Share
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3'''


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head == None:
        return head
    
    prev = head
    curr = head.next
    
    
    
    while curr != None:
        if prev.val == curr.val:
            prev.next = curr.next
            curr = curr.next
        else :
            curr = curr.next
            prev = prev.next
    
    return head