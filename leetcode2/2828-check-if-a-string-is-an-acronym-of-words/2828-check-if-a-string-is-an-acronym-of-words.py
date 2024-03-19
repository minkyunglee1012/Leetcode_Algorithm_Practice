class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        first_chr = []
        
        for i in range(len(words)):
            first_chr.append(words[i][0])
            
        if ''.join(first_chr) == s:
            return True
        else:
            return False