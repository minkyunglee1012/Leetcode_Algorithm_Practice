class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        setnum = list(set(nums))
        # print(setnum)
        for i in range(len(setnum)):
            if nums.count(setnum[i]) >= 3:
                return False
        else:
            return True