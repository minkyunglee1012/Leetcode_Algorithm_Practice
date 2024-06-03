class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = [-1] * (len(distance))
        
        n = len(s)
        
        for i in range(n):
            index = ord(s[i]) - ord('a')
            
            if dist[index] == -1:
                dist[index] = i
            else:
                if distance[index] != (i - dist[index] - 1):
                    return False
                
        return True