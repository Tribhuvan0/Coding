class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lst = []
        lst_1 = []
        lst_final = []
        for i in nums1:
            if i not in nums2 and i not in lst:
                lst.append(i)
        lst_final.append(lst)
        for i in nums2:
            if i not in nums1 and i not in lst_1:
                lst_1.append(i)
        lst_final.append(lst_1)
        return lst_final
        
        