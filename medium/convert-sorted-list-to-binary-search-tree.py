# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


## Solution 1 - Slow & fast pointers + Recursion + Pre-order traversal 
## Time Complexity: O(NlogN)
## Space Complexity: O(logN)
class Solution:
    def sortedListToBST(self, head):
        '''
        :type head: ListNode
        :rtype: TreeNode
        '''
        if not head: return
        if not head.next: return TreeNode(head.val)
        # find the mid node:
        # when fast is at the end, slow will be in the mid
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # cut the parts from mid
        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


## Solution 2 - Convert to lc108
## Get the time complexity down by using more space.
## Time Complexity: O(N)
## Space Complexity: O(N) for the lst
class Solution:
    def sortedListToBST(self, head):
        '''
        :type head: ListNode
        :rtype: TreeNode
        '''
        if not head: return
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return self.build(lst, 0, len(lst)-1)

    def build(self, lst, left, right):
        if left > right: return None
        mid = (left + right) // 2
        root = TreeNode(lst[mid])
        root.left = self.build(lst, left, mid-1)
        root.right = self.build(lst, mid+1, right)
        return root


## Solution 3 - Inorder Traversal
## Note: This solution is difficult to understand. I prefer preorder traversals.
## Time Complexity: O(N)
## Space Complexity: O(logN) for the recursion stack
class Solution:
    def sortedListToBST(self, head):
        '''
        :type head: ListNode
        :rtype: TreeNode
        '''
        ## find the size of the linked list
        curr, size = head, 0
        while curr:
            size += 1
            curr = curr.next

        def convert(left, right):
            nonlocal head
            if left > right:
                return None

            mid = (left + right) // 2
            left = convert(left, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = convert(mid + 1, right)
            return node

        return convert(0, size-1)
