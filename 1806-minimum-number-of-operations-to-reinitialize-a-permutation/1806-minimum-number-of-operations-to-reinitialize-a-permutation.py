class Solution:
    def reinitializePermutation(self, n: int) -> int:
        arr = [i for i in range(n)]
        perm = [i for i in range(n)]
        total = 0

        while total == 0 or perm != arr:
            perm = [perm[i//2] if i%2 == 0 else perm[n//2+(i-1)//2] for i in range(n)]
            total += 1 

        return total 
        