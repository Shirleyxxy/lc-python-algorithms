## Solution 1: Sorting
## Time Complexity: O(NlogN)
## Sorting costs O(NlogN) and comparing two strings costs O(N).
## Sorting time dominates and the overall time complexity is O(NlogN).
## Space Complexity: O(1) - No extra space needed
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        return sorted(s) == sorted(t)


## Solution 2: Hash Table (using two dictionaries)
## Time Complexity: O(N)
## Space Complexity: O(1)
## Note: we do use extra space, but the space complexity is O(1) since the table's size
## stays constant no matter how large n is. (Both s and t contain only letters from a to z.)
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        d1, d2 = {}, {}
        for char in s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
        for char in t:
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1
        return d1 == d2


## A more elegant way to use two dictionaries
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        d1, d2 = {}, {}
        for item in s:
            d1[item] = d1.get(item, 0) + 1
        for item in t:
            d2[item] = d2.get(item, 0) + 1
        return d1 == d2


## using Counter
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        return Counter(s) == Counter(t)


## Solution 3: Hash Table (using 1 dictionary)
## Use this solution for interviews
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            if ch not in d:
                return False
            else:
                d[ch] -= 1

        for val in d.values():
            if val != 0:
                return False
        return True
