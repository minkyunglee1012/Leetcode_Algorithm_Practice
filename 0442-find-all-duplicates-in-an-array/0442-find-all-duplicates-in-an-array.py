class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set_nums, answer = set(), []
        for n in nums:
            if n in set_nums: 
                answer.append(n)
            else: 
                set_nums.add(n)
        return answer