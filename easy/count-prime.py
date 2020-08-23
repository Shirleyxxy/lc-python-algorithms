## straightforward but time limit exceeded
## Time complexity: O(N*N)

class Solution:
    def countPrimes(self, n):
        '''
        Counts the number of prime numbers less than a non-negative number, n.
        :type n: int
        :rtype: int
        '''
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        '''
        Checks if n is a prime number.
        :type n: int
        :rtype: True/False
        '''
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

## better solution
## https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

class Solution:
    def countPrimes(self, n):
        '''
        Counts the number of prime numbers less than a non-negative number, n.
        :type n: int
        :rtype: int
        '''
        # initialize a boolean array
        isPrime = [True] * n
        for i in range(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count
