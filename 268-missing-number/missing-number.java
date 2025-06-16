class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int missing = len;
        for(int i = 0; i < len; i++){
            missing = missing ^ i ^ nums[i];
        }
        return missing;
    }
}