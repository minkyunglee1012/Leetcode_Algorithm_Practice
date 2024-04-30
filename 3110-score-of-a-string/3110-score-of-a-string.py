class Solution:
    def scoreOfString(self, s: str) -> int:
        str = 'abcdefghijklmnopqrstuvwxyz'
        asciii = [i for i in range(97, 97+26)]

        answer = 0
        for i in range(1, len(s)):
            answer += abs(asciii[str.index(s[i])] - asciii[str.index(s[i-1])])

        return answer