class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(speed):
            hr = 0
            for pile in piles:
                hr += math.ceil(pile / speed)
            return hr <= h
        
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low
                               