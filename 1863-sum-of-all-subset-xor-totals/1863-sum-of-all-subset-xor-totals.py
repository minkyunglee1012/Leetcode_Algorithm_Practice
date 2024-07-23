class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        output = 0
        for i in range(1 << len(nums)):
            s = 0
            for j in range(len(nums)):
                if i >> j & 1:
                    s ^= nums[j]
            
            output += s
            
        return output