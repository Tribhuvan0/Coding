class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = int(n*(n+1)/2)
        res = 0
        for i in range(len(nums)):
            res += nums[i]
        
        return range_sum - res
        