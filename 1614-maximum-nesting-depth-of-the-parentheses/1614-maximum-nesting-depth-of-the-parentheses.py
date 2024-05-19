class Solution:
    def maxDepth(self, s: str) -> int:
        output = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                if cnt > output :
                    output = cnt
                cnt -=1

        return output