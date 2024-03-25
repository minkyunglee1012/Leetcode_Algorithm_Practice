class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # return ' '.join(s)[::-1].split(' ')/
        
        s[:] = s[::-1]
        