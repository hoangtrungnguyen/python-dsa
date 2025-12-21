class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {


        // start at the middle: base
        // pointer 1 (p1): p1 = 0
        // case 1: sum (base, nums[p1]) < 0
        // p2 = nums.size - 1
        // move p2 until nums[base] == (nums[p1] + nums [p2]); if p2 == base; invalid
        // loop 2:
        // p1 = 1

        // case 2: sum(base, nums[p1]) > 0
        // p2 = p1 + 1
        // move p2 until sum(base, p1, p2) == 0; return when triplet when there is
        // if p2 == base: invalid

        val result = mutableSetOf<List<Int>>()

        nums.sort()
        // println(nums.joinToString())
        var base = 1      // while (base > 0) {
        // println("base ${base}")
        var pLeft = base -1
        var pRight = base + 1
        
        while(base < nums.size - 1){
            var curSum = sum3(nums, base, pLeft, pRight)

            while(pLeft >= 0 && pRight < nums.size){
                curSum = sum3(nums, base, pLeft, pRight)
                if(curSum == 0){
                    addRes(nums, result, base, pLeft, pRight)
                    pLeft -= 1
                    pRight += 1

                } else if (curSum < 0){
                    pRight += 1
                } else {
                    pLeft -= 1
                }

            }

            base += 1
            pLeft = base - 1
            pRight = base + 1
        }
        

        return result.toList()
    }

    private fun sum3(nums: IntArray, i1: Int, i2: Int, i3: Int): Int {
    
        val sum =  listOf<Int>(i1, i2, i3).filter { it >= 0 }.sumOf { nums[it] }
        // println("i1 ${i1} ${i2} ${i3}. Sum=${sum}")
        return sum
    }

    private fun addRes(nums: IntArray, result: MutableSet<List<Int>>, i1: Int, i2: Int, i3: Int) {
    
        // println("Sorted nums: ${nums.contentToString()}")
        // println("okay triplet indexes: ${i1}, ${i2}, ${i3} ")
        // println("Their values: i1=${nums[i1]}, i2=${nums[i2]}, i3=${nums[i3]}")
        
        result.add(
            listOf<Int>(
                nums[i1],
                nums[i2],
                nums[i3],
            ).sorted()
        )
    }
}

