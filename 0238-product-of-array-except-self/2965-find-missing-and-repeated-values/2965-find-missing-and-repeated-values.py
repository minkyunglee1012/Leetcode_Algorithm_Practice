class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        val = [i for i in range(1, len(grid) ** 2+1)]
        
        check = []
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                check.append(grid[i][j])
        check = sorted(check)
        
        for q in range(len(check)-1):
            if check[q] == check[q+1]:
                ans.append(check[q])
        
        for k in range(len(val)):
            if val[k] not in check:
                ans.append(val[k])
                
        return ans