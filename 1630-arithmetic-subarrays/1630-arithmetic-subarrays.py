class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        query = []
        for i in range(len(l)):
            query.append(nums[l[i]:r[i]+1])

        answer = []
        # print(query)
        for i in range(len(query)):
            check = []
            query[i] = sorted(query[i])
            # print(query[i])
            for j in range(1, len(query[i])):
                if query[i][j] - query[i][j-1] != query[i][1] - query[i][0]:
                    check.append(False)
                    # print(check)
            if check:
                answer.append(False)
            else:
                answer.append(True)

        return answer
