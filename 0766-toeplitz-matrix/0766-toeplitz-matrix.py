class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        FLAG = False
        # 대각선이 한 번이라도 다르면, False로 변경
        result = True

        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    FLAG = True
                    result = False
                    break
            if FLAG:
                break

        return result
