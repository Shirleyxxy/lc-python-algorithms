## Time Complexity: O(N)
## Space Complexity: O(1)

class ListNode:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        '''
        :type head: ListNode
        :rtype: boolean
        '''
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False
