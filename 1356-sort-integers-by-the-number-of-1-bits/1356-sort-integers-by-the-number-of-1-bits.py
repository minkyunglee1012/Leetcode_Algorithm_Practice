class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        output = list(arr)
        output.sort(key=lambda x: (bin(x).count('1'), x))

        return output