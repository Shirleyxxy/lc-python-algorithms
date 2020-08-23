class Solution:
    def removeOuterParentheses(self, S):
        '''
        :type S: str
        :rtype: str
        '''
        output = ''
        balance = 0
        start = 0
        for i in range(len(S)):
            if S[i] == '(':
                balance += 1
            elif S[i] == ')':
                balance -= 1
            if balance == 0:
                output += S[start+1:i]
                start = i + 1
        return output
