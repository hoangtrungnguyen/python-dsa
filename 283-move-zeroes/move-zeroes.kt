class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var start = 0
        var end = start + 1
        while(end < nums.size){
            val temp = nums[start]
            if(temp == 0 && nums[end] != 0){
                nums[start] = nums[end]
                nums[end] = temp
            } else if(temp == 0 && nums[end] == 0){
                end += 1
            } else {
                start += 1
                end = start + 1
            }
        }
    }
}