# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


## Time complexity: O(N) per query
## Space complexity: O(1)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])



## Cumulative sum
## Time complexity: O(1) per query, O(N) time pre-computation
## Space complexity: O(N)
class NumArray:
    def __init__(self, nums: List[int]):
        self.cumsum = [0]
        for n in nums:
            self.cumsum.append(n + self.cumsum[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.cumsum[right+1] - self.cumsum[left]
