class Solution:
    def countKeyChanges(self, s: str) -> int:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        cnt = 0
        for i in range(1, len(s)):
            if s[i] in upper:
                if s[i-1] in lower:
                    if upper.index(s[i]) == lower.index(s[i-1]):
                        pass
                    else: cnt += 1
                elif s[i] == s[i-1]:
                    pass
                else: cnt += 1
            else:
                if s[i-1] in upper:
                    if lower.index(s[i]) == upper.index(s[i-1]):
                        pass
                    else: cnt += 1
                elif s[i] == s[i-1]:
                    pass
                else : cnt += 1

        return cnt
