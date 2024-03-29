class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def comb(arr, n):
            result = []
            if n == 0:
                result.append([])
                return result
            elif n == 1:
                return [[arr[i]] for i in range(len(arr))]

            for i in range(len(arr)):
                val = arr[i]
                rest_comb = comb(arr[i+1:], n-1)

                for cb in rest_comb:
                    result.append([val] + cb)

            return result

        answer = []
        # nums = [1, 2, 3]
        for i in range(0, len(nums) + 1):
            answer += comb(nums, i)
        return answer