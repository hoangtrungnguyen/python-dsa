class Solution {
    fun intToRoman(num: Int): String {
        var number = num + 1
        val romanTable = sortedMapOf<Int, String>(
            1 to "I",
            4 to "IV",
            5 to "V",
            9 to "IX",
            10 to "X",
            40 to "XL",
            50 to "L",
            90 to "XC",
            100 to "C",
            400 to "CD",
            500 to "D",
            900 to "CM",
            1000 to "M",
        )

        var roman = StringBuilder()

//        println("Keys: ${romanTable.keys.reversed()}")
        for(key in romanTable.keys.reversed()) {
            if(number <= 0){
                break
            }
            while(number > key && number > 0){
                roman.append(romanTable[key])
                number -= key
            }
        }

        return roman.toString()
    }
}