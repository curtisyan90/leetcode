# Writing without references - Apr 14, 2022

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        
        if l1 != None and l2 != None:
            l3.val=l1.val+l2.val
            if l3.val>=10:
                l3.val-=10
                if l1.next != None: l1.next.val+=1
                elif l2.next != None: l2.next.val+=1
                else: l1.next=ListNode(1)
            l3.next=self.addTwoNumbers(l1.next,l2.next)
        elif l1 != None:
            l3.val=l1.val
            if l3.val>=10:
                l3.val-=10
                if l1.next != None: l1.next.val+=1
                else: l1.next=ListNode(1)
            l3.next=self.addTwoNumbers(l1.next,None)
        elif l2 != None:
            l3.val=l2.val
            if l3.val>=10:
                l3.val-=10
                if l2.next != None: l2.next.val+=1
                else: l2.next=ListNode(1)
            l3.next=self.addTwoNumbers(None,l2.next)
        else:
            return
        return l3
