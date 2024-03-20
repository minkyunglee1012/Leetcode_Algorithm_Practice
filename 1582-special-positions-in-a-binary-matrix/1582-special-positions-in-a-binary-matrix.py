class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        transpose = [[0]*len(mat) for _ in range(len(mat[0]))]

        one_idx = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                transpose[j][i] = mat[i][j]
                if mat[i][j] == 1:
                    one_idx.append([i, j])
        # print(transpose)
        # print(one_idx)
        cnt = 0
        for i in range(len(one_idx)):
            if sum(mat[one_idx[i][0]]) == 1 and sum(transpose[one_idx[i][1]]) == 1:
                cnt += 1

        return cnt
