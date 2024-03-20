class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []

        for idx, val in enumerate(groupSizes):
            if val not in groups:
                groups[val] = []
                # print(groups)
            groups[val].append(idx)
            # print(groups)

            if len(groups[val]) == val:
                result.append(groups[val])
                groups[val] = []
            # print(result)

        return result
