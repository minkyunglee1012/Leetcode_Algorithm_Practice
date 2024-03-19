class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = 0
        b_num = 0
        for i in range(len(a)):
            if int(a[i]) != 0:
                a_num += (2 ** int(len(a) -1 - i))
        
        for j in range(len(b)):
            if int(b[j]) != 0:
                b_num += (2 ** int(len(b) - 1 - j))
            
        num = a_num + b_num
        
        return bin(num)[2:]
