class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        for i in set(nums):
            if len(output)<=2:
                if nums.count(i)==1:
                    output.append(i)
            else:
                break
        return output