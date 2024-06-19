class Solution:
    def minimumChairs(self, s: str) -> int:
        
        
        cnt = 0
        chairs= 0
        
        for i in range(len(s)):
            if s[i] == 'E':
                cnt += 1
            else:
                chairs = max(cnt, chairs)
                cnt -=1
        
        chairs = max(cnt, chairs)
        return chairs

