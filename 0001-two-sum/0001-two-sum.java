class Solution {
    public int[] twoSum(int[] nums, int target) {
        int m=0;
        int n = 0;
        for(int i = 0; i<nums.length; i++){
            for(int j=i+1; j< nums.length; j++){
                if(nums[i]+nums[j]==target){
                    m = i;
                    n = j;
                }
            }
        }
        return new int[]{m,n};
    }
}