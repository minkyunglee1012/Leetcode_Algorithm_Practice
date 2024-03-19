class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_num1 = list(set(nums1))
        set_num2 = list(set(nums2))
        common = []
        for i in range(len(set_num1)):
            if set_num1[i] in set_num2:
                common.append(set_num1[i])
                
        return common