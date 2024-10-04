class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s_list = [i for i in s]
        return len(set(s_list))