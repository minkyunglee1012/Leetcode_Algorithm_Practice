class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original) :
            return []
        
        array_2d = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                array_2d[i][j] = original[0]
                original.pop(0)
                
        return array_2d