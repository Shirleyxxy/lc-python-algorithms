## Time Complexity: 3^3 = 27, not more than 27 combinations to check
## Space Complexity: constant space to keep the solutions
class Solution:
    def restoreIpAddresses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        if len(s) < 4 or len(s) > 12: return []
        res = []
        # dots[i] is the index of the 1st char in s AFTER the i-th dot
        # e.g., for 192.168.0.1, we have dots = [3,6,7]
        dots = []

        def backtracking():
            if len(dots) == 3 and self.isValidIPNumber(s[dots[2]:]):
                res.append(self.formatIPAddress(dots, s))
            else:
                start = dots[-1] if len(dots) > 0 else 0
                for end in range(start, min(start+3, len(s)-1)):
                    if self.isValidIPNumber(s[start:end+1]):
                        dots.append(end+1)
                        backtracking()
                        dots.pop()
        backtracking()
        return res

    def isValidIPNumber(self, s):
        if len(s) == 0 or len(s) > 3: return False
        if len(s) > 1 and s[0] == '0': return False
        return int(s) <= 255

    def formatIPAddress(self, dots, s):
        return '.'.join([s[:dots[0]], s[dots[0]:dots[1]], s[dots[1]:dots[2]], s[dots[2]:]])



class Solution:
    def restoreIpAddresses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        if len(s) < 4 or len(s) > 12: return []
        res = []
        def backtracking(s, cnt, path, res):
            if cnt == 4 and not s:
                res.append(path[:-1])
                return
            for i in range(1, 4):
                if i > len(s): continue
                if i > 1 and s[0] == '0': continue
                if i > 2 and int(s[:3]) > 255: continue
                backtracking(s[i:], cnt+1, path+s[:i]+'.', res)

        backtracking(s, 0, '', res)
        return res



## My Solution 
class Solution:
    def restoreIpAddresses(self, s):
        '''
        :type s: str
        :rtype: List[str]
        '''
        if len(s) < 4 or len(s) > 12: return []

        def isValid(s):
            if len(s) == 0 or len(s) > 3 or (len(s) > 1 and s[0] == '0') or int(s) > 255:
                return False
            return True

        def backtracking(s, cnt, path, res):
            if cnt == 4 and not s:
                res.append(path[:-1])
                return
            else:
                for i in range(1, min(4, len(s)+1)):
                    if isValid(s[:i]):
                        backtracking(s[i:], cnt+1, path+s[:i]+'.', res)

        res = []
        backtracking(s, 0, '', res)
        return res
