class Solution:
    def maxNumberOfBalloons(self, text):
        '''
        :type text: str
        '''
        balloon_counter = collections.Counter('balloon')
        text_counter = collections.Counter(text)
        result = float('inf')
        for k, v in balloon_counter.items():
            if k not in text_counter:
                return 0
            result = min(result, text_counter[k] // v)
        return result


class Solution:
    def maxNumberOfBalloons(self, text):
        '''
        :type text: str
        '''
        word = 'balloon'
        return min(text.count(k) // word.count(k) for k in set(word))
