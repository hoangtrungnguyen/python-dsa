class Solution {
    public int singleNumber(int[] nums) {
        int single = 0;
        for(int num : nums){
            single = single ^ num;
        }
        return single;
    }
}