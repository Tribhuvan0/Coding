class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #one pass solution
        numMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numMap:
                return [i,numMap[diff]]
            numMap[nums[i]] = i
                
    #Two pass solution
    def twoSumPass(self, nums,target):
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i
        
        for i in range(len(nums)):
            number = target - nums[i]
            if number in numMap and numMap[number] != i:
                return [i, numMap[number]]
        return []
        