## 1. Sort the list of products
## 2. Binary search the position of each prefix of the search word
## 3. Check if the following 3 words are valid suggestions

## Sorting and searching cost O(N * M * logN) and O(L * M * logN) respectively.
## Time Complexity: O((N + L) * M * logN)
## Space Complexity: O(L * M), including return list suggestions, but excluding
## space cost of sorting
## M = average length of products, N = len(products), L = len(searchWord)

class Solution:
    def suggestedProducts(self, products, searchWord):
        '''
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        '''
        products.sort()
        suggestions, prefix = [], ''
        for ch in searchWord:
            curr = []
            prefix += ch
            idx = self.binary_search(products, prefix)
            for i in range(idx, min(len(products), idx+3)):
                if products[i].startswith(prefix):
                    curr.append(products[i])
            suggestions.append(curr)
        return suggestions


    def binary_search(self, arr, target):
        '''
        bisect.bisect_left implementation.
        '''
        start, end = 0, len(arr)-1
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start


## We can use the built-in function for binary search
class Solution:
    def suggestedProducts(self, products, searchWord):
        '''
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        '''
        products.sort()
        suggestions, prefix = [], ''
        for ch in searchWord:
            curr = []
            prefix += ch
            idx = bisect.bisect_left(products, prefix)
            for i in range(idx, min(len(products), idx+3)):
                if products[i].startswith(prefix):
                    curr.append(products[i])
            suggestions.append(curr)
        return suggestions
