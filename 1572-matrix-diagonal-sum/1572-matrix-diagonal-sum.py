class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        cross_sum = 0




        if len(mat) % 2 == 0:
            for i in range(len(mat)):
                cross_sum += mat[i][i]
                cross_sum += mat[i][len(mat)-1-i]
        else:
            for i in range(len(mat)):
                cross_sum += mat[i][i]
                cross_sum += mat[i][len(mat)-1-i]
            cross_sum -= mat[len(mat)//2][len(mat)//2]


        return cross_sum 