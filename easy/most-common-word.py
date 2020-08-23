## Review:
## Regular expressions, re functions, collections.Counter

class Solution:
    def mostCommonWord(self, paragraph, banned):
        '''
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        '''
        words = re.findall(r'\w+', paragraph.lower())
        #words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        d = {}
        for word in words:
            if word not in banned:
                d[word] = d.get(word, 0) + 1
        return max(d, key = d.get)


class Solution:
    def mostCommonWord(self, paragraph, banned):
        '''
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        '''
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]
