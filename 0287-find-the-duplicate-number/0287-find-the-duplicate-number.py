class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
        
        for k,v in hashMap.items():
            if v > 1:
                return k
        