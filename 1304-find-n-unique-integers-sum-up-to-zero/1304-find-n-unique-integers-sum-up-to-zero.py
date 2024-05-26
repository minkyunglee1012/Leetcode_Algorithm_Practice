class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []

        for i in range(1, n//2 + 1):
            output.append(i)
            output.append(-i)
            
        if n % 2 != 0:
            output.append(0)
            
        return output  