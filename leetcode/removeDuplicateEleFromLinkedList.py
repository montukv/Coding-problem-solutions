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


class node:
    def __init__ (self,data= None):
        self.data = data
        self.next = None


class linked:
    def __init__ (self):
        self.head = node()      

    def accept(self,data):          
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        

    def deleteDuplicates(self) :
        head = self.head
        if head == None:
            return head
        
        prev = head
        curr = head.next
        
        while curr != None:
            if prev.data == curr.data:
                prev.next = curr.next
                curr = curr.next
            else :
                curr = curr.next
                prev = prev.next
        
        

    def display(self):
        disp = []
        cur = self.head
        while cur.next != None :
            cur = cur.next
            disp.append(cur.data)
        print(disp)


l_list = linked()       
s = input("enter the size of linked list")
for i in range(int(s)):
        l_list.accept(input())
l_list.deleteDuplicates()
l_list.display()
        



