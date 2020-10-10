# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Iterative
## Time Complexity: O(M + N)
## Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        # create a dummy head
        dummy_head = curr = ListNode(0)
        # while both linked lists are not empty
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # once we reach the end of a linked list, append the other list since
        # we know it is already sorted
        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1
        return dummy_head.next


## Recursive
## Time Complexity: O(M + N)
## There will be exactly one call to mergeTwoLists per element in each list
## Space Complexity: O(M + N)
class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        '''
        if not l1: return l2
        if not l2: return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
