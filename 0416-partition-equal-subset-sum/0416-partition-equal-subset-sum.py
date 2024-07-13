class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        
        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for j in dp:
                nextDP.add(j+nums[i])
                nextDP.add(j) #so that current elements are not lost
            dp = nextDP
        
        return True if target in dp else False
        