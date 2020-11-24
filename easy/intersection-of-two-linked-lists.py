# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Two Pointers
## Intuition
## headA = A + M (M is the merged part)
## headB = B + M (M is the merged part)
## To get to the intersection point (start of M) from headA, we traverse A + M + B.
## To get to the intersection point (start of M) from headB, we traverse B + M + A.

## Time Complexity: O(M + N)
## Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA, headB):
        '''
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        '''
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

## Two ways to get out of the loop:
## 1. pA and pB meet and either one would be the node we are looking for
## 2. pA and pB do not meet and they would eventually reach the end; pA == pB == None and we can return either one
