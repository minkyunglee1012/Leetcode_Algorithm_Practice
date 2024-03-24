class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        transpose = [[0]*len(grid) for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                transpose[j][i] = grid[i][j]

        row = [sum(grid[i]) - (len(grid[i]) - sum(grid[i])) for i in range(len(grid))]
        col = [sum(transpose[j]) - (len(transpose[j]) - sum(transpose[j])) for j in range(len(transpose))]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = row[i] + col[j]

        return grid