## Combination of three problems:
## 1. Middle of the linked list
## 2. Reverse linked list
## 3. Merge two sorted lists

## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


    def reorderList(self, head):
        '''
        Do not return anything, modify head in-place instead.
        :type head: ListNode
        '''
        if not head or not head.next: return
        # find the middle node of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node; reverse the second half
        second_half_head = self.reverse(slow)
        # reorder the linked list
        while second_half_head.next:
            temp = head.next
            head.next = second_half_head
            head = temp
            temp = second_half_head.next
            second_half_head.next = head
            second_half_head = temp
