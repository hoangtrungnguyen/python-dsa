class Solution {
    fun hammingWeight(number: Int): Int {
        var n = number
        var count = 0
        while( n > 0){
            n = n and (n-1)
            count ++
        }

        return count
    }
}