## Brute force (without tables)
## Time Complexity: O(N^3)
## Space Complexity: O(1) if not considering the output matrix C
class Solution:
    def multiply(self, A, B):
        '''
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        '''
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        a, b, c = len(A), len(A[0]), len(B[0])
        if b != len(B):
            raise Exception('The number of columns in A is not equal to the number of rows in B.')
        C = [[0 for _ in range(c)] for _ in range(a)]

        for i in range(a):
            for j in range(c):
                for k in range(b):
                    C[i][j] += A[i][k] * B[k][j]
        return C


## Optimize using the sparsity
## Time Complexity: O(N^2)
class Solution:
    def multiply(self, A, B):
        '''
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        '''
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        a, b, c = len(A), len(A[0]), len(B[0])
        if b != len(B):
            raise Exception('The number of columns in A is not equal to the number of rows in B.')
        C = [[0 for _ in range(c)] for _ in range(a)]

        sparse_A = self.get_sparse_matrix(A)
        sparse_B = self.get_sparse_matrix(B)
        for i_A, j_A, el_A in sparse_A:
            for i_B, j_B, el_B in sparse_B:
                if j_A == i_B:
                    C[i_A][j_B] += el_A * el_B
        return C

    def get_sparse_matrix(self, mat):
        sparse_mat = []
        for i, row in enumerate(mat):
            for j, el in enumerate(row):
                if el:
                    sparse_mat.append((i, j, el))
        return sparse_mat


## With tables
## Time Complexity: O(N^3)
class Solution:
    def multiply(self, A, B):
        '''
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        '''
        if not A or not B: return None
        a, b, c = len(A), len(A[0]), len(B[0])
        if b != len(B):
            raise Exception('The number of columns in A is not equal to the number of rows in B.')
        C = [[0 for _ in range(c)] for _ in range(a)]

        table_B = {}
        for i, row in enumerate(B):
            table_B[i] = {}
            for j, el_B in enumerate(row):
                if el_B:
                    table_B[i][j] = el_B

        for i, row in enumerate(A):
            for k, el_A in enumerate(row):
                if el_A:
                    for j, el_B in table_B[k].items():
                        C[i][j] += el_A * el_B
        return C
