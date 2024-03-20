class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for idx in range(len(words)):
            if words[idx].startswith(pref):
                count += 1

        return count
