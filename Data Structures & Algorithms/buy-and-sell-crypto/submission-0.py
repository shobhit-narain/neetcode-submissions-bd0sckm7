class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for price in prices[1:]:
            lowest = min(price, lowest)
            res = max(res, price-lowest)
        return res