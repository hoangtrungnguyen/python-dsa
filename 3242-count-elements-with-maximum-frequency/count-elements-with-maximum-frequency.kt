
class Solution {
    fun maxFrequencyElements(nums: IntArray): Int {
        val frequencies = IntArray(101)
        var maxCount = 0
        var total = 0
        for(i in nums.indices){
            val value = nums[i]
            frequencies[value] = frequencies[value] + 1
            if(frequencies[value]!! > maxCount){
                maxCount = frequencies[value]!!
                total = frequencies[value]!!
            } else if (frequencies[value] == maxCount) {
                total += frequencies[value]!!
            }
        }

        return total
    }
}