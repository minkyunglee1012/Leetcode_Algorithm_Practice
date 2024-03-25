class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pop_val = nums.pop(0)
            if pop_val in nums:
                nums.append(pop_val)
                continue
            return pop_val
                
        