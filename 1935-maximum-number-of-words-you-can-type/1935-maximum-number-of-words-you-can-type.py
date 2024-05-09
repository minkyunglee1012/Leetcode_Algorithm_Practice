class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        cnt = 0
        for t in text:
            for b in brokenLetters:
                if b in t:
                    cnt += 1
                    break

        return len(text)-cnt