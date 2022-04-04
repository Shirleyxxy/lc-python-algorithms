## Dictionary
## Time complexity: O(N)
## Space complexity: O(N)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and i - cache[num] <= k:
                return True
            cache[num] = i
        return False


## Set
## Space optimization using a fixed-size set with a least recently seen eviction policy
## Time complexity: O(N)
## Space complexity: O(K)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
