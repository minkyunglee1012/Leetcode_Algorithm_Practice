class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i+2 <= len(grid)-1 and j+2 <= len(grid[0]) -1:
                    hourglass.append(sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3]))

        return max(hourglass)