class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        set_num = []

        for i in range(len(nums)):
            if (i < len(nums)-1 and nums[i] not in (nums[:i] + nums[i+1:])) or (i == len(nums)-1 and nums[i] not in nums[:i]):
                set_num.append(nums[i])

        return sum(set_num) 