class Solution:
    def isPalindrome(self, s: str) -> bool:
        digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

        s = ''.join(s.split(' '))

        for i in range(len(s)):
            if s[i] not in digits:
                s = s.replace(s[i], ' ')
        s = ''.join(s.split(' '))
        s = s.lower()
        if s == s[::-1]:
            return True
        return False