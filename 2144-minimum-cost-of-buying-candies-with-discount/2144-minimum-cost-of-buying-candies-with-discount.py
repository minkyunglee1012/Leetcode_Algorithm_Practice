class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            # print(sum(cost))
            return sum(cost)

        cost = sorted(cost)[::-1]
        # print(cost)
        return sum(cost) - sum(cost[2::3])