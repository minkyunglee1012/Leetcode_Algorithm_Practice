class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # 계산해야 하는 알파벳 수
        alpha_num = digits.index(s[3]) - digits.index(s[0]) + 1
        
        # 계산해야 하는 숫자
        num = int(s[-1]) - int(s[1]) + 1
        
        # 총 순회해야 하는 횟수
        need_for = alpha_num * num
        
        result = []
        
        for i in range(alpha_num):
            for j in range(num):
                a = digits[digits.index(s[0]) + i]
                b = str(j + int(s[1]))
                result.append(a+b)
                
        return result
        
