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
    def findDisapearedNumbers(self, nums: List[int]) -> List[int]:
        lsti = []
        lst = [0]*(len(nums)+1)
        for i in nums:
            lst[i] += 1
        for i in range(1,len(nums)+1):
            if lst[i] == 0:
                lsti.append(i)
        return lsti
                