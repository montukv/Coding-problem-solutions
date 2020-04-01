
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      if(not l1 and l2):
          return(l2)
      if(l1 and not l2):
          return(l1)
      term1 = l1
      term2 = l2
      head = None
      temp1 = None
      temp2 = None
      while(term1 and term2):
          if(term1.val < term2.val):
              if(term1 == l1 and head == None):
                  head = l1
              while(term1 and term1.val <= term2.val):
                  prevTerm = term1
                  term1 = term1.next
              prevTerm.next = term2
          if(term1 and term2 and term2.val < term1.val): 
              if(term2 == l2 and head == None):
                  head = l2
              while(term2 and term2.val <= term1.val):
                  prevTerm = term2
                  term2 = term2.next
              prevTerm.next = term1
          if(term1 and term2  and term1.val == term2.val):
              if(term1 == l1):
                  head = term1
              while(term1 and term2 and term1.val == term2.val):
                  prevTerm = term1
                  term1 = term1.next
              prevTerm.next = term2 
      return(head)
