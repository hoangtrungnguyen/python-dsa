class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sort()
        // println("nums ${nums.joinToString(",")}")
        for(i in nums.size - 1 downTo 2){
            if(nums[i - 1] + nums[i - 2]> nums[i]){
                return nums[i-1] + nums[i-2] + nums[i]
            }
        }

        return 0
    }
}