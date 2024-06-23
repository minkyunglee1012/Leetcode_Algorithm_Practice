class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        palindrome_num = str(x)
        
        
        if palindrome_num == palindrome_num[::-1]:
            return True
        return False
