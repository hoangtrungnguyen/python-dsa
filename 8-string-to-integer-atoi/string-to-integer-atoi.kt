class Solution {
    fun myAtoi(s: String): Int {
        var sb = StringBuilder()
        var signed = 0
        for (i in 0 until s.length) {
            // println("signed: ${signed}")
            // println("${s[i]}")
            // println("${s[i].code}")

            if (s[i] == ' ' && signed != 0) {
                break
            } else if (s[i] == ' ' && sb.isEmpty()) {

            } else if (s[i].code == 48 && sb.isEmpty() && signed != 0) {
                sb.append(s[i])
            } else if (s[i] == '-' && signed == 0) {
                signed = -1
            } else if (s[i] == '+' && signed == 0) {
                signed = 1
            } else if (s[i].code in 48..57) {
                sb.append(s[i])
                if (signed == 0) {
                    signed = 1
                }
            } else {
                break
            }
            // println("---")
        }
        if (signed == 0) {
            signed = 1
        }
        return if (sb.isEmpty()) {
            0
        } else {
            // println(sb.toString())
            // println("signed :${signed}")
            //.toInt()

            // return -1

            //2147483647
            // val longNum = sb.toString().trim().toLong()
            var numStr = sb.trimStart('0').toString()
            // println("${sb.trimStra('0')}")
            if (numStr.length == 0) {
                return 0
            }

            if (numStr.length < 10) {
                return numStr.toInt() * signed
            } else if (numStr.length > 10) {
                return if (signed == -1) {
                    return Int.MIN_VALUE
                } else {
                    return Int.MAX_VALUE
                }
            } else {
                val longNum = numStr.toLong() * signed
                // println("longNum :${longNum}")
                if (longNum >= Int.MAX_VALUE) {
                    return Int.MAX_VALUE
                } else if (longNum <= Int.MIN_VALUE) {
                    // println("Int.MIN_VALUE: ${Int.MIN_VALUE}")
                    return Int.MIN_VALUE
                } else {
                    return longNum.toInt()
                }
            }

        }
    }

}

// fun main() {
    // println(Solution().myAtoi("  +  413"))
// }