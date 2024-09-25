class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1, num2, num3 = str(num1), str(num2), str(num3)
        
        if len(num1) != 4:
            num1 = '0' * (4-len(num1)) + num1
        
        if len(num2) != 4:
            num2 = '0' * (4-len(num2)) + num2
        
        if len(num3) != 4:
            num3 = '0' * (4-len(num3)) + num3
        
        key_number = ''
        for i in range(4):
            key_number += str(min(int(num1[i]), int(num2[i]), int(num3[i])))
            
        return int(key_number)