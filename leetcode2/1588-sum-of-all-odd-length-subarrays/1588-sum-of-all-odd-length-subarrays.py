class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        result = 0
        n = len(arr)
        while n > 0:
            if n == 1:
                result += sum(arr)
                break
                
            if n > 1 and n % 2 == 1:
                for i in range(len(arr)-n+1):
                    result += sum(arr[i:i+n])
                n -= 2
            else:
                n -= 1

            
            
        return result