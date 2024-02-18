class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
                
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
            
        return result