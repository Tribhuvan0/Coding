class Solution {
    public void sortColors(int[] nums) {
        int[] arr = new int[3];
        Arrays.fill(arr,0);
        for(int i: nums){
            arr[i]++;
        }
        int i = 0;
        int j = 0;
        while(i<arr.length){
            while(arr[i]!=0){
                nums[j] = i;
                arr[i]--;
                j++;
            }
            i++;
        }
    }
}