class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        min_LR = [0] * len(height)

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i+1])

        for i in range(len(maxRight)):
            min_LR[i] = min(maxRight[i], maxLeft[i])

        water = 0

        for i in range(len(height)):
            temp = 0
            temp += max((min_LR[i] - height[i]), 0)
            water += temp
            
        return water
        