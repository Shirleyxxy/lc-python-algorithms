## Time Complexity: O(N)
## Space Complexity: O(1)

class Solution:
    def deleteDuplicates(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


class Solution:
    def deleteDuplicates(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        curr = head
        while curr:
            # keep skipping duplicated nodes
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
