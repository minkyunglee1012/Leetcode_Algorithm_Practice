class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        k_diff = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    if nums[i] <= nums[j]:
                        k_diff.append((nums[i], nums[j]))
                    else:
                        k_diff.append((nums[j], nums[i]))
        
        return len(set(k_diff))
