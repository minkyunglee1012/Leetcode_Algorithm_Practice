class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        transposed = [[0] * row for _ in range(col)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                transposed[j][i] = matrix[i][j]

        return transposed
