class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = []
        odd = []

        for i in range(len(position)):
            if position[i]%2 == 0:
                even.append(position[i])
            else:
                odd.append(position[i])

        return min(len(even), len(odd))