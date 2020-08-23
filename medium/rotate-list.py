## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        '''
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        '''
        if not head: return None
        if not head.next: return head

        # count the number of nodes
        n, old_tail = 1, head
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        # close the linked list into a ring
        old_tail.next = head

        new_tail = head
        # n-k%n-1
        for i in range(n - k%n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None
        return new_head
