class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets, curSet = [], []
        
        self.helper(0,nums,subSets,curSet)
        return subSets
    
    def helper(self,i,nums,subSets,curSet):
        if i >= len(nums):
            subSets.append(curSet.copy())
            return
        
        #To include the particular element
        curSet.append(nums[i])
        self.helper(i+1, nums, subSets, curSet)
        curSet.pop()
        
        #To not include the particular element
        self.helper(i+1, nums, subSets, curSet)
    
    
        
        
        