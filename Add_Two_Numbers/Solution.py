# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summation = l1.val+l2.val
        c = 0
        if summation >=10:
            sum_value = summation%10
            c = summation //10
            summation = sum_value
            
        head = ListNode(summation)
        result = head
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            if not l1:
                summation = l2.val
                l2 = l2.next
                
            elif not l2:
                summation = l1.val
                l1 = l1.next
                
            else:
                summation = l1.val+l2.val
                l1 = l1.next
                l2 = l2.next
            
            if (summation+c) >=10:
                sum_value = (summation+c)%10
                c = (summation+c)//10
                summation = sum_value
                result.next = ListNode(summation)
                result = result.next
                continue
                

            result.next = ListNode(summation+c)
            result = result.next
            c = 0

        if c > 0 :
            result.next = ListNode(c)
        
        return head
        
