class Solution:
    def minOperations(self, n: int) -> int:
        if (n-1) % 2 == 0:
            return sum([i for i in range(0, n, 2)])
        else:
            return sum([i for i in range(1, n, 2)])
