class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        for i in range(1, n+1):
            if sum([k for k in range(1, i+1)]) == sum([p for p in range(i, n+1)]):
                return i
        return -1
