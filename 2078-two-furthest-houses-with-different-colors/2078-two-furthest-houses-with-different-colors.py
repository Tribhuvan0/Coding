class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = -inf
        for i in range(len(colors)):
            for j in range(len(colors)-1,-1,-1):
                if colors[i] != colors[j] and max_dist < abs(i-j):
                    max_dist = abs(i-j)
        return max_dist
        