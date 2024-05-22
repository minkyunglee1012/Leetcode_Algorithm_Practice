class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        absolute_difference = {}

        for i in range(len(arr) -1):
            if (arr[i+1] - arr[i]) not in absolute_difference:
                absolute_difference[arr[i+1] - arr[i]] = [[arr[i], arr[i+1]]]
            else:
                absolute_difference[arr[i+1] - arr[i]] += [[arr[i], arr[i+1]]]

        return absolute_difference[min(absolute_difference.keys())]