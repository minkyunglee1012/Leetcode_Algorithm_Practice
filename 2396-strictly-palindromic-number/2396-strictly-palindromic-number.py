class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        base = 2
        num = n
        while base <= n-2:
            
            num_str = ''
            while num > 0:
               remain = str(num % base)
               num_str = remain + num_str
               if num == 1 :
                   break
               num = num // base
            
            if num_str == num_str[::-1]:
                base += 1
                num =n
            else:
                return False
            
        return True
