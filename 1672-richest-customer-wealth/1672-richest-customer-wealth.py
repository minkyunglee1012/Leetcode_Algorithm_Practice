class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = []

        for i in range(len(accounts)):
            if sum(accounts[i]) > sum(max_sum):
                max_sum = accounts[i]

                
        return sum(max_sum)
