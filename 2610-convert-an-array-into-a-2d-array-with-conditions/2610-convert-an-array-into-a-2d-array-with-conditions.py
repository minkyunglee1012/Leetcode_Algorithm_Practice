class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        while max(nums) > 0:
            stack = []
            for i in range(len(nums)):
                if nums[i] > 0 and nums[i] not in stack:
                    stack.append(nums[i])
                    nums[i] = 0
            result.append(stack)
            
            
        return result
