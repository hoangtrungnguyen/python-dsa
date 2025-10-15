import kotlin.math.pow

class Solution {
    fun reverse(x: Int): Int {

        // x = 0
        // result = 0
        // 123 % 10 = 3
        // result += 3

        // 12 % 10 = 2
        // result = result * 10 = 30
        // result += 2  = 32

      
        var result: Double = 0.0
        var y = x
        var decimal = 0
        while( y != 0){
            val remain = y % 10
            result = result * (10.0)
            result += (remain)
            if (result > Int.MAX_VALUE || result < Int.MIN_VALUE){
                return 0
            }
            y /= 10
            decimal ++
            // println("y: ${y}, remain: ${remain}")
        }

        return result.toInt()

    }
}