class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt = 0 
        summ = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                cnt += 1
                summ += nums[i]
                
        if cnt == 0:
            return 0
        else:
            return int(summ/cnt)