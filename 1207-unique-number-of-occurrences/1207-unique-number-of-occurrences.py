class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for i in arr:
            if i not in occurrences:
                occurrences[i] = 1
            else:
                occurrences[i] += 1
        
        return sorted(list(occurrences.values())) == sorted(list(set(occurrences.values())))
           