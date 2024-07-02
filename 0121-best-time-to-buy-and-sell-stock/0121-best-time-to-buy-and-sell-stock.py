class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
            else:
                res = max((prices[r] - prices[l]), res)
                r += 1
        return res
                
        