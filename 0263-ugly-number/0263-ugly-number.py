class Solution:
    def isUgly(self, n: int) -> bool:
        
        prime_factors = [2, 3, 5]
        
        for f in prime_factors:
            while n > 1 and n % f == 0:
                n = n // f
        
        if n == 1:
            return True
        return False
