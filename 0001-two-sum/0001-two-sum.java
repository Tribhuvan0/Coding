class Solution {
    public int[] twoSum(int[] nums, int target) {
        int m = 0;
        int n = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            map.put(nums[i],i);
        }
        for(int j = 0; j<nums.length; j++){
            int rest = target - nums[j];
            if(map.containsKey(rest)){
                if(map.get(rest) == j){
                    continue;
                }
                else{
                    m = j;
                    n = map.get(rest);
                    break;
                }
            }
        }
        return new int[]{m,n};
    }
}