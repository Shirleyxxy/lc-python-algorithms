## Similar to lc83 - Remove duplicates from sorted list
## Dummy nodes
## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def removeElements(self, head, val):
        '''
        :type head: ListNode
        :type val: int
        '''
        dummy_head = ListNode(0)
        dummy_head.next = head

        prev, curr = dummy_head, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy_head.next
