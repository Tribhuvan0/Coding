class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curres = [], []
        self.helper(0,candidates,target,res,curres,0)
        return res
    
    def helper(self,i,candidates,target,res,curres,cur_sum):
        if cur_sum == target:
            res.append(curres.copy())
            return
        if i >= len(candidates) or cur_sum > target:
            return
        
        curres.append(candidates[i])
        #This condition adds the same element multiple times to the result
        self.helper(i, candidates,target, res,curres,cur_sum+candidates[i])
        curres.pop()
        
        #THis picks the next element
        self.helper(i+1, candidates,target,res,curres,cur_sum)
        