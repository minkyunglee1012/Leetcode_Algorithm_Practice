class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        single_digit = []
        double_digit = []
        
        for i in range(len(nums)):
            if nums[i] < 10:
                single_digit.append(nums[i])
            else:
                double_digit.append(nums[i])
                
        if sum(single_digit) == sum(double_digit):
            return False
        return True
        