class Solution {
    public int majorityElement(int[] nums) {
        int counter = 0;
        int number = -1;
        for(int num: nums){
            if(counter == 0){
                counter = 1;
                number = num;
            } else if (number == num){
                counter += 1;
            } else {
                counter -= 1;
            }
        }
        return number;
    }
}