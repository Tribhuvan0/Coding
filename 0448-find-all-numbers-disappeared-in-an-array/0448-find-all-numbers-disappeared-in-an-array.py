class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            n = abs(i) - 1
            nums[n] = -1*(abs(nums[n]))
        lst = []
        for i,n in enumerate(nums):
            if n > 0:
                lst.append(i+1)
        return lst