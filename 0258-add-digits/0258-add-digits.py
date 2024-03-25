class Solution:
    def addDigits(self, num: int) -> int:
        
        if num < 10:
            return num
        
        while num >= 10:
            num_sum = 0
            num_list = list(str(num))
            
            for i in range(len(num_list)):
                num_sum += int(num_list[i])
                
            num = num_sum
            
        return num