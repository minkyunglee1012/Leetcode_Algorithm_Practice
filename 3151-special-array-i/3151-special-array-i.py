class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        cnt = 0
        
        for i in range(len(nums)-1):
            if (nums[i] + nums[i+1]) %2 == 0:
                cnt += 1
                
                
        return cnt == 0