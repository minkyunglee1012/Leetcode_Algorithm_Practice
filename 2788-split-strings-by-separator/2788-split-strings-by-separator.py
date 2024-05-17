class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for i in range(len(words)):
            split_words = words[i].split(separator)
            for j in range(len(split_words)):
                if split_words[j] != "":
                    answer.append(split_words[j])
        return answer