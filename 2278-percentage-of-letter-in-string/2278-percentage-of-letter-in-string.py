class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0 

        for i in range(len(s)):
            if letter == s[i]:
                cnt += 1

        return int((cnt / len(s)) * 100)