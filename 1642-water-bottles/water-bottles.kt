class Solution {
       fun numWaterBottles(numBottles: Int, numExchange: Int): Int {
//        val init = numBottles
//        return  init +
//        println("Num water bottles: $numBottles")
                return recursion(numBottles , numExchange) + numBottles
    }

    private fun recursion(numBottles: Int, numExchange: Int): Int {
        if (numBottles < numExchange) {
            return 0
        }
        val exchanges = numBottles / numExchange
//        println("recursion - numBottles:$numBottles, numExchange:$numExchange, exchanges:$exchanges")

        var remain = 0
        if (numBottles > numExchange) {
            remain = numBottles % numExchange
        }
        return exchanges + recursion(
            exchanges + remain, numExchange
        )
    }
}