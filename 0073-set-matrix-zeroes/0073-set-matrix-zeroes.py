class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_index.append([i, j])

        for z in zero_index: 
            matrix[z[0]] = [0] * len(matrix[z[0]])  # 행의 모든 원소를 0으로 변경
            for row in matrix:
                row[z[1]] = 0  # 열의 모든 원소를 0으로 변경

        return matrix
        
