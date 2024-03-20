class Solution:
    def checkXMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == j or (i + j) == len(matrix) - 1:
                    if matrix[i][j] == 0:
                        return False

                elif matrix[i][j] != 0:
                    return False

        
        return True
                

#             if matrix[i][i] == 0:
#                 return False
#             if matrix[i][len(matrix)-1-i] == 0:
#                 return False
            
#             for j in range(len(matrix[i])):
#                 if i != j and matrix[i][j] != 0:
#                     return False
                    
#         return True
