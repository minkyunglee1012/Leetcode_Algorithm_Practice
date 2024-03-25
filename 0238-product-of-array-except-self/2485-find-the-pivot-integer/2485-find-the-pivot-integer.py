class Solution:
    def pivotInteger(self, n: int) -> int:
        num_list = []
        for i in range(n):
            num_list.append(i+1)
        
        if n == 1:
            return 1
        
        result = 0
        for j in range(1, len(num_list)):
            if sum(num_list[:j]) == sum(num_list[j - 1:]):
                result = num_list[j-1]
  
        if result == 0:
            result = -1
            
        return result