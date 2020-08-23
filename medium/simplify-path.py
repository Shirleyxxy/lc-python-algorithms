## Time Complexity: O(N)
## Space Complexity: O(N)

class Solution:
    def simplifyPath(self, path):
        '''
        :type path: str
        :rtype: str
        '''
        if not path: return ''
        path_ls = path.split('/')
        stack = []
        for el in path_ls:
            if el == '.' or el == '':
                continue
            elif el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        return '/' + '/'.join(stack)
