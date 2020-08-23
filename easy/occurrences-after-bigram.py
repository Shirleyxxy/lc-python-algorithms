# my solution 
class Solution:
    def findOcurrences(self, text, first, second):
        '''
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        '''
        output = []
        text_list = text.split()
        for i in range(len(text_list)-2):
            if text_list[i] == first and text_list[i+1] == second:
                output.append(text_list[i+2])

        return output
