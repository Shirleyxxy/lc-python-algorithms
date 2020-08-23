# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Time Complexity: O(max(M, N))
## Space Complexity: O(max(M, N))
## The length of the new list is at most max(M, N) + 1.

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        dummy_head, carry = ListNode(0), 0
        curr = dummy_head
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            curr.next = ListNode(sum % 10)
            carry = sum // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next
