class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count_sum = 0
        for i in range(1, n+1):
            if i % 3 == 0:
                count_sum += i
            elif i % 5 == 0:
                count_sum += i
            elif i % 7 == 0:
                count_sum += i
                
        return count_sum