class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        for n in nums:
            if n%2 == 0:
                s += n

        output = []
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                s -= nums[queries[i][1]]

            nums[queries[i][1]] += queries[i][0]

            if nums[queries[i][1]] % 2 == 0:
                s += nums[queries[i][1]]

            output.append(s)

        return output