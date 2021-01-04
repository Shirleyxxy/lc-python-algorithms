## DFS Preorder:
## Node --> Left --> Right
## The height-balanced restriction means that at each step one has to pick up the number
## in the middle as a root. That works fine with arrays containing odd number of elements
## but there is no predefined choice for arrays with even number of elements.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## We can slice an array recursively, but slicing the array is expensive.
## It is better to pass the left and right bounds into recursive calls instead.

## Time Complexity: O(N)
## Space Complexity: O(N) - O(N) to keep the output and O(logN) for the recursion stack
class Solution:
    def sortedArrayToBST(self, nums):
        '''
        :type nums: List[int]
        :rtype: TreeNode
        '''
        if not nums: return None
        return self.build(nums, 0, len(nums)-1)


    def build(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.build(nums, left, mid-1)
        node.right = self.build(nums, mid+1, right)
        return node
