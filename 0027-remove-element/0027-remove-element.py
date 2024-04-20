class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        i,j =0,0
        while i< len(nums)-1:
            if nums[i] != val:
                i += 1
                j += 1
            elif nums[i] == val:
                i += 1
                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j],nums[i]
                    j += 1
        for i in nums:
            if i == val:
                cnt += 1
        return len(nums) - cnt
                    
                
            
        