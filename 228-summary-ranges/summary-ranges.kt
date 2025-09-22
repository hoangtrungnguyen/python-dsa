class Solution {
    fun summaryRanges(nums: IntArray): List<String> {
        var s:Int = 0
        var e:Int = 0
        val n = nums.size
        if(n == 0){
            return emptyList<String>()
        }
        val result = mutableListOf<String>()
        while( e < n){
            if(e > s && (nums[e]-nums[e - 1]!=1) ){
                if(s != e - 1){
                    result.add("${nums[s]}->${nums[e-1]}")
                    s = e 
                } else {
                    result.add("${nums[s]}")
                    s = e
                }
            } else {
                e += 1
            }
        }
        // println("s: ${s}")
        // println("e: ${e}")
        if(s == e - 1){
            result.add("${nums[s]}")
        } else {
            result.add("${nums[s]}->${nums[e-1]}")
        }
        return result
    }
}