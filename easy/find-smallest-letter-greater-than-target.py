## Time Complexity: O(logN)
## Space Complexity: O(1)

class Solution:
    def nextGreatestLetter(self, letters, target):
        '''
        :type letters: List[str]
        :type target: str
        :rtype: str
        '''
        start, end = 0, len(letters)-1
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        # circular list 
        return letters[start % len(letters)]
