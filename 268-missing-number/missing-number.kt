class Solution {
    fun missingNumber(nums: IntArray): Int {
        val l = nums.size
        var expectedSum = ( l * (l+1)) / 2
        for(i in 0 until l){
            expectedSum -= nums[i]
        }
        return expectedSum

        var i = 0
        while(i < l) {
            val tmp = nums[i]
            if( tmp < l && tmp >= 0){
                nums[i] = nums[tmp]
                nums[tmp] = tmp
            } else {
                i += 1
            }
                    println(nums.joinToString(", "))

        }
        for( i in 0 until l){
            if(nums[i] < 0 || nums[i] > l){
                return i           
            }
        } 
        return l 

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