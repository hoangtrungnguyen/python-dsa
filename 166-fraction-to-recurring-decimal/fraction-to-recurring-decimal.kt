import kotlin.math.abs

class Solution {
    fun fractionToDecimal(num: Int, den: Int): String {

//        println("${numerator.toDouble() / denominator.toDouble()}")
        val numerator = num.toLong()
        val denominator = den.toLong()
        val sb = StringBuilder()

        // sb: StringBuilder
        // map: integer -> index (based on sb.length)
        // remain = numerator % denominator
        // while remain > 0:
        //
        //    map[remain] -> sb.length
        //    remain = (remain * 10) / denominator

        if(numerator == 0L){
            return "0"
        }

        val N = abs(numerator / denominator)
        sb.append(N)

        if((numerator < 0) xor (denominator < 0)){
            sb.insert(0, "-")
        }


        val remainToIndex = mutableMapOf<Long, Int>()

        var remain = numerator % denominator

        // println("remain: $remain")

        if (remain != 0L) {
            sb.append(".")
            // println("sb: ${sb.toString()}")
        }


        while (remain != 0L) {
            // println("remain: $remain")
            if (remainToIndex.containsKey(remain)) {
                sb.insert(remainToIndex[remain]!!,"(")
                sb.append(")")
                break
            }

            remainToIndex[remain] = sb.length
            remain = remain * 10
            val fraction = remain / denominator
            val newRemain = remain % denominator
            sb.append("${abs(fraction)}")
            remain = newRemain
        }

        return sb.toString()
    }
}