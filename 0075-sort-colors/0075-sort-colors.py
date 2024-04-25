class Solution:
    def srtColors(self, nums: List[int]) -> None:
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
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #One pass solution using partition logic, we are not incrementing pointer
        #as incrementing pointer in case of right_ptr can cause 0 to be undetected
        left_ptr, right_ptr = 0, len(nums) - 1
        i = 0
        while i <= right_ptr:
            if nums[i] == 0:
                nums[left_ptr], nums[i] = nums[i], nums[left_ptr]
                left_ptr += 1
            
            elif nums[i] == 2:
                nums[right_ptr], nums[i] = nums[i], nums[right_ptr]
                right_ptr -= 1
                i -= 1
            i += 1
                
            
        