## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


    def isPalindrome(self, head):
        '''
        :type head: ListNode
        :rtype: boolean
        '''
        if head is None or head.next is None: return True
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node; reverse the second half
        second_half_head = self.reverse(slow)
        # compare the first and the second half
        while second_half_head:
            if head.val != second_half_head.val:
                return False
            head = head.next
            second_half_head = second_half_head.next
        return True
