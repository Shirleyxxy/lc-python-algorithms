## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        '''
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        '''
        if not head or k < 2: return head
        curr, prev = head, None
        while True:
            prev_last_node = prev
            curr_last_node = curr
            count = 0
            # check if there are k nodes in the sublist
            while curr and count < k:
                curr = curr.next
                count += 1
            # reverse k nodes
            if count == k:
                curr = curr_last_node
                for i in range(k):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                # connect with the previous part
                if prev_last_node:
                    prev_last_node.next = prev
                else:
                    head = prev
                # connect with the next part
                curr_last_node.next = curr

            if curr is None: break
            prev = curr_last_node

        return head
