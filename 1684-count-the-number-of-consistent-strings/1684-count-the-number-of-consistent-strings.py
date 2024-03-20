class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    words[i] = words[i].replace(words[i][j], '-')

        cnt = 0
        for i in range(len(words)):
            # print(words)
            if '-' not in words[i]:
                cnt += 1

        return cnt
