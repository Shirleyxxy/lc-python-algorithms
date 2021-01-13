## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def defangIPaddr(self, address):
        '''
        :type address: str
        :rtype: str
        '''
        return '[.]'.join(address.split('.'))
