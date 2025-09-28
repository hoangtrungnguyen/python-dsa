class Solution {
    fun largestPerimeter(origin: IntArray): Int {
        var nums = origin.sorted()
        // println("nums ${nums.joinToString(",")}")
        for(i in nums.size - 1 downTo 0){
            val a = nums[i]
            for( j in i - 1 downTo 0){
                val b = nums[j]
                for(k in j - 1 downTo 0){
                    val c = nums[k]
                    if(isTriangle(a,b,c)){
                        return a + b + c
                    }
                }
            }
        }

        return 0
    }

    private fun isTriangle(a: Int, b: Int, c:Int): Boolean{
        return (a + b) > c && (b + c) > a && (a + c) > b
    }
}