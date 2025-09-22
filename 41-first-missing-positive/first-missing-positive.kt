
class Solution {
    fun firstMissingPositive(nums: IntArray): Int {
        var i = 0
        val n = nums.size
        while (i < n) {
            //.   if nums[i] != i + 1 || nums[i] != -1
            //       value = nums[i]
            //.      corrected_value = nums[value-1]
            //.      if(value >= n){
            //.       nums[i] = -1
            // } else{
            //.      nums[i] = corrected_value
            //.      nums[value- 1] = value
            //.   }
            //    else
            //.      i += 1
            val correctIndex = nums[i] - 1
          if (nums[i] > 0 && correctIndex < n && nums[i] != nums[correctIndex]) {
                val temp = nums[i]
                nums[i] = nums[correctIndex]
                nums[correctIndex] = temp
            } else {
                i += 1
            }

        }

        // println("nums ${nums.joinToString(",")}")
        for( j in nums.indices){
            if(nums[j] != j + 1){
                return j + 1
            }
        }
        return n + 1
    }
}

// 1. set element to the right index
//  1 -> index = 0
//  2 -> index = 1
//. [1,2,0] -> [0,1,2]
//  [3, 4, -1, 1] -> [1, -infinite, 3, 4,]
//  [3,4,-1,1] -> [1,-1,3,4]
//. [7,8,9,11,12] -> [-1,-1, -1, -1, -1]
//  [-3, 2, 0, 1, 4] -> [1, 2, -1, 4, -1]