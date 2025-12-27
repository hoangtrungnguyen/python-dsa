class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        // Sort the array to enable the two-pointer approach
        nums.sort()
        
        // Initialize the closest sum with the first possible triplet
        var closestSum = nums[0] + nums[1] + nums[2]

        var distance = -1

        // Iterate through the array, using 'anchor' as the first element of the triplet
        for (anchor in 0 until nums.size - 2) {
            // Use two pointers for the remaining two elements
            var p1 = anchor + 1
            var p2 = nums.size - 1

            while (p1 < p2) {
                val currentSum = sum3(nums, anchor, p1, p2)
                
                // If the exact target is found, return immediately
                if (currentSum == target) {
                    return currentSum
                }

    
                // Update closestSum if the current triplet is closer to the target
                if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
                    closestSum = currentSum
                } 

            
                // Move pointers based on whether the sum is smaller or larger than the target
                if (currentSum < target) {
                    p1++ // Increase sum by moving left pointer forward
                    while(p1 < p2 && nums[p1- 1] == nums[p1]) p1++
                } else {
                    p2-- // Decrease sum by moving right pointer backward
                    while(p2 > p1 && nums[p2 + 1] == nums[p2]) p2--
                }
            }
        }
        return closestSum
    }

    /**
     * Helper function to calculate the sum of three elements at specific indices
     */
    private fun sum3(nums: IntArray, i1: Int, i2: Int, i3: Int): Int {
        return nums[i1] + nums[i2] + nums[i3]
    }
}