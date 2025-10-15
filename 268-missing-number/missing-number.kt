class Solution {
    fun missingNumber(nums: IntArray): Int {
        val n = nums.size
        var i = 0
        while(i < n) {
            val correctIndex = nums[i]
            
            // If the number is a valid index (0 to n-1) and is not
            // already in its correct spot, we perform a swap.
            if (correctIndex < n && nums[i] != nums[correctIndex]) {
                val temp = nums[i]
                nums[i] = nums[correctIndex]
                nums[correctIndex] = temp
            } else {
                i += 1
            }
        }
        for( i in 0 until n){
            if(nums[i] < 0 || nums[i] >= n){
                return i           
            }
        } 
        return n

    }
}

// l = nums.length
// for i in 0 until n:
//   value = nums[i]
//   if (l != value)
//.     nums[i] = i
//      nums[value] = value
//   else:
//      nums[i] = -1
//

fun main(){
    Solution().missingNumber(intArrayOf(1,2,3))
}