class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        for i in range(len(words1)):
            if words2.count(words1[i]) == 1 and words1.count(words1[i]) == 1:
                cnt += 1
        return cnt