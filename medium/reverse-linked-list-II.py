## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, m, n):
        '''
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        '''
        if m == n: return head
        # skip the first m-1 nodes
        curr, prev = head, None
        i = 0
        while curr and i < m - 1:
            prev = curr
            curr = curr.next
            i += 1

        prev_list_last = prev
        curr_list_last = curr

        # reverse [m, n] nodes
        i = m - 1
        while curr and i <= n - 1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        # connect with the previous sublist
        if prev_list_last:
            prev_list_last.next = prev
        else:
            head = prev
        # connect with the next sublist
        curr_list_last.next = curr
        return head 
