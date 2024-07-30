class Solution:
    def minimumDeletions(self, s: str) -> int:
        output = 0
        cnt = 0
        
        for i in s:
            if i == 'b':
                cnt += 1
            elif cnt:
                output += 1
                cnt -= 1
                
        return output
        