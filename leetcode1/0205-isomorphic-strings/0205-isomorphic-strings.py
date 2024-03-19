class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_idx = []
        t_idx = []
        for idx in s:
            s_idx.append(s.index(idx))
        for idx in t:
            t_idx.append(t.index(idx))
        if s_idx == t_idx:
            return True
        return False
            