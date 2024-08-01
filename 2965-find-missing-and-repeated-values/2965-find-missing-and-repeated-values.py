class Solution:
    def findMissingAndRepeatedValues(self,grid):
        ROWS, COLS = len(grid), len(grid[0])
        arr = []
        for i in range(ROWS):
            for j in range(COLS):
                arr.append(grid[i][j])
        arr.sort()
        for i in range(1,len(arr)+1):
            if arr[i-1] == arr[i]:
                extraNum = arr[i]
                break
        missingNum = len(arr)*(len(arr) + 1)//2 -  (sum(arr) - extraNum)
        return [extraNum, missingNum]