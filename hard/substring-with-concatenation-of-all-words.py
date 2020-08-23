## Time Complexity: O(N * M)
## Space Complexity: O(M)

class Solution:
    def findSubstring(self, s, words):
        '''
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        '''
        if len(words) == 0 or len(words[0]) == 0 or s == '': return []
        result_indices = []
        words_cnt, word_len = len(words), len(words[0])
        # Store the frequency of every word in a dictionary
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Starting from every index in the string, try to match all the words
        for i in range((len(s) - words_cnt * word_len) + 1):
            words_seen = {}
            for j in range(0, words_cnt):
                next_word_index = i + j * word_len
                word = s[next_word_index : next_word_index + word_len]
                # Break if we do not need this word
                if word not in word_freq: break

                # Add the word to the "words_seen" dictionary
                words_seen[word] = words_seen.get(word, 0) + 1

                # Break if the word has higher frequency than required
                if words_seen[word] > word_freq[word]: break

                # Store index if we have found all the words
                if j + 1 == words_cnt: result_indices.append(i)

        return result_indices
