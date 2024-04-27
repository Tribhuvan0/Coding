class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        freq = {}
        for i in range(0, len(nums)):
            if nums[i] not in dicti:
                dicti[nums[i]] = 1
            else:
                dicti[nums[i]] += 1
        
        for z,v in dicti.items():
            if v not in freq:
                freq[v] = [z]
            else:
                freq[v].append(z)
        
        arr = []
        
        for x in range(len(nums), 0, -1):
            if x in freq:
                for i in freq[x]:
                    arr.append(i)
        
        return [arr[x] for x in range(0, k)]
        