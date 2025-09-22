class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        var mergedArr = mutableListOf<Int>()
        var totalLength = nums1.size + nums2.size
        var medianIndex1: Int
        var medianIndex2: Int? = null
        if (totalLength % 2 == 1) {
            medianIndex1 = totalLength / 2
        } else {
            medianIndex1 = totalLength / 2 - 1
            medianIndex2 = medianIndex1 + 1
        }
        // println("medianIndex1 ${medianIndex1}")
        // println("medianIndex2 ${medianIndex2}")

        var i = 0
        var j = 0
        while (i < nums1.size || j < nums2.size) {
            if ( i < nums1.size && j < nums2.size ){
            if (nums1[i] < nums2[j]) {
                mergedArr.add(nums1[i])
                i++
            } else {
                mergedArr.add(nums2[j])
                j++
            }
            } else if ( i >= nums1.size){
                mergedArr.add(nums2[j])
                j ++
            } else if ( j >= nums2.size){
                mergedArr.add(nums1[i])
                i ++
            }

            // println("i: ${i} j: ${j} - mergedArr: ${mergedArr.joinToString(",")}")
            if(medianIndex2 == null){
                if (medianIndex1 == mergedArr.size - 1  ) {
                    return mergedArr.last().toDouble()
                }
            } else {
                if(medianIndex2 == mergedArr.size - 1){
                    // if( nums1[i] < nums2[j]){
                //         mergedArr.add(nums1[i])
                //     } else {
                //         mergedArr.add(nums2[j])
                //     }
                    return (mergedArr[medianIndex2] + mergedArr[medianIndex1]) / 2.0
                }
            }
        }

        return -1.0
    }
}