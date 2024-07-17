class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output = 0
        while n > 0 :
            reminder = n % k
            output += reminder
            n = int(n / k)
            
        return output
    