class Solution {
    fun largestPerimeter(nums: IntArray): Int {
        nums.sort()
        // println("nums ${nums.joinToString(",")}")
        for(i in nums.size - 1 downTo 2){
            val a = nums[i]
            val b = nums[i - 1]
            val c = nums[i - 2]
            if(isTriangle(a,b,c)){
                return a + b + c
            }
        }

        return 0
    }

    private fun isTriangle(a: Int, b: Int, c:Int): Boolean{
        return (a + b) > c && (b + c) > a && (a + c) > b
    }
}