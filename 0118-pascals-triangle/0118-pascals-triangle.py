class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascalnums=[]
        pascalnums.append([1])
        
        for i in range(numRows - 1):
            newrow = [1]
            for j in range(i):
                newrow.append(pascalnums[i][j] + pascalnums[i][j+1])
            newrow.append(1)
            pascalnums.append(newrow)
            
        return pascalnums