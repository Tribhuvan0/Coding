class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combs, curcombs = [], []
        used = [False]*len(nums)
        self.helper(nums,used,combs,curcombs)
        return combs
    
    def helper(self,nums,used,combs,curcombs):
        if len(curcombs) == len(nums):
            combs.append(curcombs.copy())
            return
        
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                curcombs.append(nums[i])
            
                self.helper(nums,used,combs,curcombs)
            
                curcombs.pop()
                used[i] = False
        
        
        
        