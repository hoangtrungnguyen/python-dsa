import kotlin.math.max

class Solution {
    fun maxSubArray(nums: IntArray): Int {

        var maxSum = nums[0]
        var currSum = nums[0]
            
        for( i in 1 until nums.size){
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
        }
        return maxSum
    }
}