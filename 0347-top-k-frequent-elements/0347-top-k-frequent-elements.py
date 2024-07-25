class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        arr = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            dicti[n] = 1 + dicti.get(n,0)
        
        for key,val in dicti.items():
            arr[val].append(key)
        
        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
        