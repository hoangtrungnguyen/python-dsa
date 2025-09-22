class Solution {
    fun hammingWeight(number: Int): Int {
        var n = number
        var count = 0
        while( n > 0){
            if( n % 2 == 1){
                count ++
            }
            n /= 2
        }

        return count
    }
}