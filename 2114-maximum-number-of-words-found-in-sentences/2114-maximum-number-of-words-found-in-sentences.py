class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = []


        for i in range(len(sentences)):
            answer.append(len(sentences[i].split()))

        return max(answer)
