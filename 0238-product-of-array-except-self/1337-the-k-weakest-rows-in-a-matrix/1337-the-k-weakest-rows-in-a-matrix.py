class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_power = []
        
        for i in range(len(mat)):
            row_power.append(sum(mat[i]))
            
        w_s = []
        
        for j in range(len(row_power)):
            w_s.append(row_power.index(min(row_power)))
            row_power[row_power.index(min(row_power))] = 101
            
        return w_s[:k]