
class Solution {
    fun maxFrequencyElements(nums: IntArray): Int {
        val frequencies = mutableMapOf<Int, Int>()
        var maxCount = 0
        var listOfKeys = mutableListOf<Int>()
        for(i in nums.indices){
            val value = nums[i]
            frequencies.putIfAbsent(value, 0)
            frequencies[value] = frequencies[value]!! + 1
            if(frequencies[value]!! > maxCount){
                maxCount = frequencies[value]!!
                listOfKeys.clear()
                listOfKeys.add(value)
            } else if (frequencies[value] == maxCount) {
                listOfKeys.add(value)
            }
        }

        var total = 0
        for(key in listOfKeys){
            total += frequencies[key]!!
        }

        return total
    }
}