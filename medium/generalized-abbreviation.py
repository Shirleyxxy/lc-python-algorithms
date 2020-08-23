## Time Complexity: O(N * 2^N)
## Space Complexity: O(N * 2^N)

class Solution:
    def generateAbbreviations(self, word):
        '''
        :type word: str
        :rtype: List[str]
        '''
        def generateAbbreviationsRec(pos, curr, count):
            # Once we reach the end, append the current to the final result
            if pos == len(word):
                result.append(curr+str(count) if count > 0 else curr)
            else:
                # Skip the current position and increment count
                generateAbbreviationsRec(pos+1, curr, count+1)
                # Include the current position and zero-out count
                generateAbbreviationsRec(pos+1, curr + (str(count) if count > 0 else '') + word[pos], 0)

        result = []
        generateAbbreviationsRec(0, '', 0)
        return result
