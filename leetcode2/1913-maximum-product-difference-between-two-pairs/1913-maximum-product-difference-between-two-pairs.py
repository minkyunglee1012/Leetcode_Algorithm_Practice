class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_pair = []
        second_pair = []
        
        first_pair.append(max(nums))
        nums.remove(max(nums))
        first_pair.append(max(nums))
        nums.remove(max(nums))
        
        second_pair.append(min(nums))
        nums.remove(min(nums))
        second_pair.append(min(nums))
        nums.remove(min(nums))
        
        return (first_pair[0] * first_pair[1]) - (second_pair[0] * second_pair[1])
            