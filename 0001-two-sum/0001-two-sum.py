class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    lst.append(i)
                    lst.append(j)
        return lst
                
        