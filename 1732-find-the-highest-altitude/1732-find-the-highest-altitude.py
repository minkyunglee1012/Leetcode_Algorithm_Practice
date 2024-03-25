class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        altitudes = [0]
        
        for i in range(len(gain)):
            start += gain[i]
            altitudes.append(start)
            
        return max(altitudes)