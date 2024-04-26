class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicti = {}
        for i in range(len(nums1)):
            dicti[nums1[i]] = i
        lst = [-1]*len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in dicti:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = dicti[nums2[i]]
                    lst[idx] = nums2[j]
                    break
        return lst