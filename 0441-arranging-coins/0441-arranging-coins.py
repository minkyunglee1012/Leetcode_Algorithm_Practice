class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: return 1
        
        count = 0
        for i in range(1, n):
            n -= i
            count += 1
            if n <= i:
                break
                
        return count
            
