class Solution:
    def findLatestTime(self, s: str) -> str:
        s = [i for i in s]
        print(s)

        if s[0] == '?':
            if s[1] == '?':
                s[0] = '1'
            elif int(s[1]) < 2:
                s[0] = '1'
            else :
                s[0] = '0'

        if s[1] == '?':
            if int(s[0]) == 1:
                s[1] = '1'
            else:
                s[1] = '9'

        if s[3] == '?':
            s[3] = '5'

        if s[4] == '?':
            s[4] = '9'

        output = ''
        for i in s:
            output += i

        return output