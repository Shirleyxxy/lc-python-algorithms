## Solution 1: Fast & slow pointers
## Time Complexity: O(N)
## Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findCycleLength(self, slow):
        '''
        :type slow: ListNode
        :rtype: int
        '''
        curr = slow
        cycle_length = 0
        while True:
            curr = curr.next
            cycle_length += 1
            if curr == slow: break
        return cycle_length


    def findCycleStart(self, head, cycle_length):
        '''
        :type head: ListNode
        :type cycle_length: int
        :rtype: ListNode
        '''
        pointer1, pointer2 = head, head
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1


    def detectCycle(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle_length = self.findCycleLength(slow)
                return self.findCycleStart(head, cycle_length)
        return None


## Solution 2: Set
## Find the first node we have seen before.

## Time Complexity: O(N)
## Space Complexity: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        '''
        :type head: ListNode
        :rtype: ListNode
        '''
        seen = set()
        while head:
            if head in seen:
                return head
            else:
                seen.add(head)
                head = head.next
        return None
