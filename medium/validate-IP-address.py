## IPv4: canonically represented in dot-decimal notation
## which consists of four decimal numbers, each ranging from 0 to 255
## separated by dots ("."), e.g.,172.16.254.1
## leading zeros in IPv4 is invalid.

## IPv6: represented as eight groups of four hexadecimal digits
## each group representing 16 bits. The groups are separated by colons (":")
## IPv6 allows omitting some leading zeros and uppercase letters.


class Solution:
    def validIPAddress(self, IP):
        '''
        :type IP: str
        :rtype: str, "IPv4" or "IPv6" or "Neither".
        '''
        def isIPv4(str):
            if str.isdigit():
                # check for leading zero
                if not (str[0] == '0' and len(str) > 1):
                    return 0 <= int(str) <= 255
            return False

        def isIPv6(str):
            if len(str) > 4 or len(str) == 0:
                return False
            return all(char in set('0123456789abcdefABCDEF') for char in str)

        if len(IP.split('.')) == 4 and all(isIPv4(sub) for sub in IP.split('.')):
            return 'IPv4'

        if len(IP.split(':')) == 8 and all(isIPv6(sub) for sub in IP.split(':')):
            return 'IPv6'

        return 'Neither'
