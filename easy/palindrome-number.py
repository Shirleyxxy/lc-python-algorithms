# my solution (converting int to string; not recommended)
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            x_ls = list(str(x))
            if x_ls == x_ls[::-1]:
                return True
            else:
                return False

# reverse number
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev_x = 0
        temp = x
        while temp != 0:
            curr = temp % 10
            rev_x = rev_x * 10 + curr
            temp = temp // 10  # integer division
        if rev_x == x:
            return True
        else:
            return False


# revert half of the number (leetcode solution)
