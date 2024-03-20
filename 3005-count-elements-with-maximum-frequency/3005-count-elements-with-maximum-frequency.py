class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        set_nums = sorted(list(set(nums)))
        count = []

        for i in range(len(set_nums)):
            count.append(nums.count(set_nums[i]))

        return count.count(max(count)) * max(count)
