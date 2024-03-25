class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        transpose = [[0]*len(grid) for _ in range(len(grid[0]))]

        for i in range(len(transpose)):
            for j in range(len(transpose[i])):
                transpose[i][j] = len(str(grid[j][i]))

        # transpose
        output = []
        for i in range(len(transpose)): 
            output.append(max(transpose[i]))

        return output