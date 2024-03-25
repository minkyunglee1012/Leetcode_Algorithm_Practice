class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i : length + i]:
                    return i
        return -1