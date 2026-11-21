class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current = prices[-1]
        i = len(prices) - 2

        while i >= 0:
            max_profit = max(current - prices[i], max_profit)

            if prices[i] > current:
                current = prices[i]
                i -= 1
            else:
                i -= 1
                
        return max_profit