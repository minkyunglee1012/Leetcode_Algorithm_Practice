class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ''

        for i in range(len(order)):
            if order[i] in s:
                ans += order[i] * s.count(order[i])

        for j in range(len(s)):
            if s[j] not in order:
                ans += s[j]

        return ans
