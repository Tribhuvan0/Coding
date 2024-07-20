class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        while k != 1:
            heapq.heappop(nums)
            k -= 1
        #res = heapq.heappop(nums) 
        
        return -nums[0]
    def findiKthLargest(self, nums,k):
        k = len(nums) - k
        
        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
        
            if p < k: return quickSelect(p+1, r)
            elif p > k: return quickSelect(l,p-1)
            else: return nums[p]
        return quickSelect(0,len(nums)- 1)
            
        
        