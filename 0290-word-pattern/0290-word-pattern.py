class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        
        pattern_idx = []
        s_idx = []
        
        for idx in pattern:
            pattern_idx.append(pattern.index(idx))
            
        for idx in s_list:
            s_idx.append(s_list.index(idx))
            
        if pattern_idx == s_idx:
            return True
        return False
