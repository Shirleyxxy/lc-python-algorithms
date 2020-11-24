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


## My solution
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
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            _sum = val1 + val2 + carry
            head.val = _sum % 10
            carry = _sum // 10
            head, head.next = ListNode(-1), head
        if carry > 0:
            head.val = carry
            head, head.next = ListNode(-1), head
        return head.next


## O(1) Space Complexity
## Reverse LinkedLists + Add Two Numbers (lc2)
class Solution:
    def reverseList(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        dummy_head, carry = ListNode(0), 0
        curr = dummy_head
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            _sum = val1 + val2 + carry
            curr.next = ListNode(_sum % 10)
            carry = _sum // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
            curr = curr.next
        return self.reverseList(dummy_head.next)
