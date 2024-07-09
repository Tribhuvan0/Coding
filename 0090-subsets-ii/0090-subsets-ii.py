class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curSet, subSets = [],[]
        self.helper(0,nums,subSets,curSet)
        return subSets
    
    def helper(self,i,nums,subSets,curSet):
        if i >= len(nums):
            subSets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i+1,nums,subSets,curSet)
        curSet.pop()
        
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1  #[1,2,2,4] so if i == 2, when it will be passed to helper will                          #be at 3
        self.helper(i+1,nums,subSets,curSet)