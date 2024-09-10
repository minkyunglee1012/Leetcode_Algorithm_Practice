class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        digit = 'abcdefghijklmnopqrstuvwxyz'
        
        cnt = 0
        
        for j in range(len(strs[0])):
            sort_check = []
            for i in range(len(strs)):
                sort_check.append(digit.index(strs[i][j]))
            
            # print(sort_check)
            if sort_check != sorted(sort_check):
                cnt += 1
                
                
        return cnt
                