class Solution:
    def numSquares(self, n: int) -> int:
        # Create a list to store the minimum number of perfect squares that sum to each value from 0 to n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be represented by 0 perfect squares

        # Iterate over all numbers from 1 to n
        for i in range(1, n + 1):
            j = 1
            # Check for all perfect squares less than or equal to i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]