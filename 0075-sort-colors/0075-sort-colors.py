class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Two pass solutions using bucket sort
        cnt_lst = [0,0,0]
        for i in nums:
            if i == 0:
                cnt_lst[0] += 1
            elif i == 1:
                cnt_lst[1] += 1
            else:
                cnt_lst[2] += 1
        
        for i in range(len(nums)):
            if cnt_lst[0] != 0:
                nums[i] = 0
                cnt_lst[0] -= 1
            elif cnt_lst[1] != 0:
                nums[i] = 1
                cnt_lst[1] -= 1
            elif cnt_lst[2] != 0:
                nums[i] = 2
                cnt_lst[2] -= 1
        
            
        