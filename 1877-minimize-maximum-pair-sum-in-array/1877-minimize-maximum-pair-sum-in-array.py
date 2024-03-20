class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)

        pair = []

        while nums:
            pair.append((nums.pop(0), nums.pop()))

        pair

        sumlist = []
        for i in range(len(pair)):
            sumlist.append(sum(pair[i]))

        return max(sumlist)
