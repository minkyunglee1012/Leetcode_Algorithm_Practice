class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        
        for i in range(len(nums)):
            if nums[i] < 10:
                digit_sum += nums[i]
                
            else:
                num_str = str(nums[i])
                for j in range(len(num_str)):
                    digit_sum += int(num_str[j])
                    
        return abs(element_sum - digit_sum)
