class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        output = []
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n and (i, j , k) not in output:
                        output.append((i, j, k))
                        
        return len(output)
        
