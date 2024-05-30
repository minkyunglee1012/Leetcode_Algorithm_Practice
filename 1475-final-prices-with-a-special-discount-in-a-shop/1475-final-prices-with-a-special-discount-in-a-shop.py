class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        for i in range(len(prices)):
            if 0 <= i < len(prices) -1 and prices[i] >= min(prices[i+1:]):
                for k in range(i+1, len(prices)):
                    if prices[i] >= prices[k]:
                        output.append(prices[i] - prices[k])
                        break
            else:
                output.append(prices[i])

        return output