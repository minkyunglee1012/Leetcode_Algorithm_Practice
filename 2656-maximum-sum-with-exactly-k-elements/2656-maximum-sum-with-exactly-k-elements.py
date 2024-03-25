class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            ans += max(nums) + i
            
        return ans