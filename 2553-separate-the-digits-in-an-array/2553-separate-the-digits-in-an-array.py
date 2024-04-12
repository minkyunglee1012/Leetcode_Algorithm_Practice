class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if nums[i] >=10:
                result += [int(n) for n in str(nums[i])]
            else:
                result.append(nums[i])

        return result