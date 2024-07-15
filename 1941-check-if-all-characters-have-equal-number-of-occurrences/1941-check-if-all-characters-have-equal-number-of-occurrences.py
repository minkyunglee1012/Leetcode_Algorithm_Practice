class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurrences = {}
        
        for i in range(len(s)):
            if s[i] not in occurrences:
                occurrences[s[i]] = 1
            else:
                occurrences[s[i]] += 1
                
        return len(set(occurrences.values())) == 1