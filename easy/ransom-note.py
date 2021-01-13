## M = length of the magazine
## N = length of the ransom note
## My Solution (1 dictionary)
## Time: O(Max(M, N))
## Space: O(K) / O(1)
class Solution:
    def canConstruct(self, ransomNote, magazine):
        '''
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        '''
        d1 = collections.defaultdict(int)
        for ch in ransomNote:
            d1[ch] += 1
        for ch in magazine:
            d1[ch] -= 1

        for k, v in d1.items():
            if v > 0:
                return False
        return True


## Similar idea
## Time: O(M)
## if M < N, we immediately return false
## the worst case occurs when M >= N
## O(M) to create a dictionary of counts for the magazine
## O(N) to iterate over the ransom note
## M >= N, so O(M) time complexity in the worst case
## Space: O(K) / O(1)
## K = number of unique characters across both the ransom note and magazine
## K is never more than 26, so O(1) is also correct
class Solution:
    def canConstruct(self, ransomNote, magazine):
        '''
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        '''
        if len(ransomNote) > len(magazine): return False
        letters = collections.Counter(magazine)
        for ch in ransomNote:
            if letters[ch] <= 0:
                return False
            letters[ch] -= 1
        return True
