class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        power_digits = 1
        sum_digits = 0
        
        for i in range(len(str_n)):
            power_digits *= int(str_n[i])
            sum_digits += int(str_n[i])
            
        return power_digits - sum_digits