class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        output = 0
        
        while min(nums) < k:
            nums.remove(min(nums))
            output += 1
            
        return output