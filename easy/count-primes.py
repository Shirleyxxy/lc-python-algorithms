## straightforward but time limit exceeded
## sequentially test each candidate number
## Time Complexity: O(N^2)

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
        O(n).
        '''
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True



## https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
## A common optimization: start enumerating the multiples of each prime i from i^2.
## Time Complexity: O(NloglogN)
class Solution:
    def countPrimes(self, n):
        '''
        Counts the number of prime numbers less than a non-negative number, n.
        :type n: int
        :rtype: int
        '''
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])
        return sum(primes)
