class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        for(int i =0; i< nums.length; i++){
            if(nums[i]>nums[(i+1)%nums.length]){
                count++;
            }
            if(count>1){ //count can only be ==1 once (peak element) if it's more than 1 then their is issue and array is not rotated sorted
                return false;
            }
        }
        return true;
    }
}