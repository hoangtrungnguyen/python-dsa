class Solution {
    fun intToRoman(num: Int): String {
     val values = arrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

    var number = num
    val roman = StringBuilder()

    for (i in values.indices) { // We loop through the indices
        // While the number is large enough...
        while (number >= values[i]) {
            // ...we append the symbol from the same index.
            roman.append(symbols[i])
            number -= values[i]
        }
    }
    return roman.toString()
    }
}