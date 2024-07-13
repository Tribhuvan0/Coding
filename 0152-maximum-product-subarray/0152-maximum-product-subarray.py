class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 1,1
        ans = float('-inf')
        
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix*nums[len(nums)-i-1]
            ans = max(ans,max(prefix,suffix))
        
        return ans
                
        