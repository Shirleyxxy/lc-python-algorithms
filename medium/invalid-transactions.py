## Brute force
## Time Complexity: O(N^2)
## Space Complexity: O(N)
class Solution:
    def invalidTransactions(self, transactions):
        '''
        :type transactions: List[str]
        :rtype: List[str]
        '''
        invalid = []
        for i in range(len(transactions)):
            name1, time1, amount1, city1 = transactions[i].split(',')
            if int(amount1) > 1000:
                invalid.append(transactions[i])

            for j in range(i+1, len(transactions)):
                name2, time2, amount2, city2 = transactions[j].split(',')
                if name2 == name1 and city2 != city1 and abs(int(time1) - int(time2)) <= 60:
                    invalid.append(transactions[i])
                    invalid.append(transactions[j])

        return list(set(invalid))



## Optimized solution
## Time Complexity: O(NlogN)
## Space Complexity: O(N)
'''
Create a transaction data structure.
'''
from collections import defaultdict

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

class Solution:
    def invalidTransactions(self, transactions):
        '''
        :type transactions: List[str]
        :rtype: List[str]
        '''
        transactions = [Transaction(*transaction.split(',')) for transaction in transactions]
        # Sort the transactions based on time, O(NlogN)
        transactions.sort(key = lambda t: t.time)

        # O(N)
        trans_d = defaultdict(list)
        for i, t in enumerate(transactions):
            trans_d[t.name].append(i)

        invalid = []
        # O(N)
        for name, indexes in trans_d.items():
            left = right = 0
            for i, trans_i in enumerate(indexes):
                t = transactions[trans_i]
                if t.amount > 1000:
                    invalid.append('{},{},{},{}'.format(t.name, t.time, t.amount, t.city))
                    continue # avoid adding duplicate transactions
                # use left, right pointers to represent the possible neighbor transactions that are within the 60 minutes
                while left <= len(indexes)-2 and transactions[indexes[left]].time < t.time - 60:
                    left += 1
                while right <= len(indexes)-2 and transactions[indexes[right+1]].time <= t.time + 60:
                    right += 1
                for i in range(left, right+1):
                    if transactions[indexes[i]].city != t.city:
                        invalid.append('{},{},{},{}'.format(t.name, t.time, t.amount, t.city))
                        break
        return invalid
