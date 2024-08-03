class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l,r = 0, len(heights) - 1
        while l < r:
            maxi = max(maxi, (r-l)*min(heights[r], heights[l]))
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxi
        