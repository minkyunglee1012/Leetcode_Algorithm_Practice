from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        transpose = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(transpose)):
            for j in range(len(transpose[i])):
                transpose[i][j] = matrix[j][i]

        min_max_list = []
        for i in range(len(matrix)):
            min_max_list.append(min(matrix[i]))

        output = []
        for j in range(len(transpose)):
            if max(transpose[j]) in min_max_list:
                output.append(max(transpose[j]))
                
        return output