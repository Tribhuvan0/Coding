class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = []
        sumRight = []
        for i in range(len(nums)):
            sumLeft.append(sum(nums[0:i+1]))
        for i in range(len(nums)):
            sumRight.append(sum(nums[i:len(nums)]))
        for i in range(len(nums)):
            if sumRight[i] == sumLeft[i]:
                return i
        return -1
            
    
                       
        