class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        l_sum = 0
        r_sum = 0
        arr = []
        
        for i in range(len(nums) - 1):
            l_sum += nums[i]
            left[i+1] = l_sum
            
        for j in range(len(nums) - 1):
            r_sum += nums[len(nums)-1-j]
            right[len(nums)-2-j] = r_sum
            
        for r in range(len(left)):
            arr.append(abs(left[r] - right[r]))
            
        return arr