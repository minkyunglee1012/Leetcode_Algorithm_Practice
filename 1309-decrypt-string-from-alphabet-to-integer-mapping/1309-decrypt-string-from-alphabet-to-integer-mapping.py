class Solution:
    def freqAlphabets(self, s: str) -> str:
        apb= 'abcdefghijklmnopqrstuvwxyz'
        answer = ''
        for i in range(len(s)):
            if i < len(s)-2 and s[i+2] == '#' :
                answer += apb[int(s[i:i+2]) -1]
            elif i < len(s)-1 and s[i+1] == '#':
                pass
            elif s[i] == '#':
                pass
            else:
                answer += apb[int(s[i]) - 1]

        return answer
