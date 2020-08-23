# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## Why inserting (node.val, i, node) rather than just (node.val, node) into the heap?
## When there is a tie in the first value of the tuple, heapq uses the second value
## as the tie breaker. But since the second value is an object of ListNode that has
## no definition of comparision, we will encounter an error.

## Time Complexity: O(NlogK)
## Space Complexity: O(K)

from heapq import *

class Solution:
    def mergeKLists(self, lists):
        '''
        :type lists: List[ListNode]
        :rtype: ListNode
        '''
        min_heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapify(min_heap)
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            val, i, node = min_heap[0]
            # exhausted one linked-list
            if not node.next:
                heappop(min_heap)
            else:
                # recycling tie-breaker i guarantees uniqueness
                heapreplace(min_heap, (node.next.val, i, node.next))
            curr.next = node
            curr = curr.next
        return dummy.next
