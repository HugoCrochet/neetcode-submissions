class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # tips : the most profitable time to buy time is when the price is at its lowest !*
        # need to track the lowest price and the max difference
        res = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest : lowest = p
            res = max(res, p - lowest)
        return res

        