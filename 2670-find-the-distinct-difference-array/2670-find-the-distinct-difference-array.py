class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
            output = []

            if len(nums) == 1:
                return [1]
            for i in range(len(nums)):
                if i == 0:
                    output.append(1 - len(set(nums[i+1:])) )
                elif 1 <= i < len(nums) - 1:
                    output.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
                else:
                    output.append(len(set(nums)))
            return output