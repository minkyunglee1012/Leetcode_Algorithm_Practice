class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num_str = '0123456789'
        s = s.split(' ')
        num_list = []

        for i in range(len(s)):
            if s[i][0] in num_str:
                num_list.append(int(s[i]))

        if len(set(num_list)) != len(num_list):
            return False
        return num_list == sorted(num_list)