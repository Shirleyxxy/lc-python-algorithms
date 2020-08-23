# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Use stack since reversing the linkedlists is not allowed.
## Similar problem: Add two numbers
## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head, carry = ListNode(-1), 0
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            carry, val = divmod(carry, 10)
            # update the ListNode value
            head.val = val
            # create a new ListNode and set the pointer to the current
            # updated ListNode
            head, head.next = ListNode(-1), head
            #temp = head
            #head = ListNode(-1)
            #head.next = temp
        return head.next
