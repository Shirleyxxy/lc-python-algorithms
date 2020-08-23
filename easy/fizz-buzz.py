## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution(object):
    def fizzBuzz(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        outputs = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                outputs.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                outputs.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                outputs.append('FizzBuzz')
            else:
                outputs.append(str(i))
        return outputs


## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def fizzBuzz(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        ans = []

        for num in range(1, n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))

        return ans


## String Concatenation
## a better way if we have more conditions to check, e.g. FizzBuzzJazz
## Time Complexity: O(N)
## Space Complexity: O(1)
class Solution:
    def fizzBuzz(self, n):
        '''
        :type n: int
        :rtype: List[str]
        '''
        ans = []

        for num in range(1, n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)

            num_ans_str = ''

            if divisible_by_3:
                num_ans_str += 'Fizz'
            if divisible_by_5:
                num_ans_str += 'Buzz'
            if not num_ans_str:
                num_ans_str += str(num)

            ans.append(num_ans_str)

        return ans
