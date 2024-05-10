class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        transpose = [[0]*len(grid) for _ in range(len(grid[0]))]
        for i in range(len(transpose)):
            for j in range(len(transpose[i])):
                transpose[i][j] = grid[j][i]
        transpose

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cnt += min(max(grid[i]), max(transpose[j])) - grid[i][j]

        return cnt