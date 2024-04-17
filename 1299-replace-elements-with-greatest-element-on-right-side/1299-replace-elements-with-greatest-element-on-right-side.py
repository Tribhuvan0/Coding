class Solution:
    def replaceElements(self, arr: List[int],min_int = -1) -> List[int]:
        for i in range(len(arr)-1, -1, -1):
            arr[i], min_int = min_int, max(min_int,arr[i])
        return arr
    