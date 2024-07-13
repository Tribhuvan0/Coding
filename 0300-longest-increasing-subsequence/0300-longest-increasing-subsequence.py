class Solution:
    def lengthiOfLIS(self, nums: List[int]) -> int:
        arr = []
        def dfs(idx, prev_idx,arr):
            if idx >= len(nums):
                return 0
            
            #not pick
            length = dfs(idx+1, prev_idx)
            
            if (prev_idx == -1) or (nums[prev_idx] < nums[idx]):
                length = max(length, 1 + dfs(idx+1, idx))
            return length
        
        return dfs(0,-1,arr)
    
    def lengthOfLIS(self, nums: List[int]):
        LIS = [1]*len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)
        
        