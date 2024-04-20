class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 0
            else:
                hash_map[nums[i]] += 1
        return [i for i in hash_map if hash_map[i]==max(hash_map.values())][0]
            
            
        