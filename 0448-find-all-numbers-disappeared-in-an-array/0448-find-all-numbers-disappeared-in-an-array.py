class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        lsti = []
        lst = [0]*(len(nums)+1)
        for i in nums:
            lst[i] += 1
        for i in range(1,len(nums)+1):
            if lst[i] == 0:
                lsti.append(i)
        return lsti
                