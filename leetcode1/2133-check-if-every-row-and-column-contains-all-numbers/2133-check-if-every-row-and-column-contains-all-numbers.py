class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        transpose = [[0]*len(matrix) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            if len(set(matrix[i])) != len(matrix[i]):
                return False
            for j in range(len(matrix[i])):
                transpose[j][i] = matrix[i][j]

        for i in range(len(transpose)):
            if len(set(transpose[i])) != len(transpose[i]):
                return False

        return True
