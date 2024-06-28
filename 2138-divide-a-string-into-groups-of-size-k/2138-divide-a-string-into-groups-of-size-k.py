class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        output = []
        for i in range(0, len(s), k):
            if len(s[i:i+k]) == k:
                output.append(s[i:i+k])
            else:
                output.append(s[i:] + ((k-len(s[i:])) * fill))
                
        return output