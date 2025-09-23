import kotlin.math.max
class Solution {
    fun compareVersion(version1: String, version2: String): Int {
        var data1 = version1.split(".").map<String, Int>{
//            it.removeLeadingZero
            it.toInt()
        }
        var data2 = version2.split(".").map<String, Int>{
            it.toInt()
        }

        if(data1.first() > data2.first()){
            return 1
        } else if(data1.first() < data2.first()){
            return -1
        } else {
            data1.drop(1)
            data2.drop(1)
            println("data1 ${data1}")
            println("data2 ${data2}")
            val len = max(data1.size, data2.size)
            for(i in 0 until len){
                if (i < data1.size && i < data2.size){
                    if(data1[i] > data2[i]){
                        return 1
                    } else if (data1[i] < data2[i]){
                        return -1
                    } else {
                        continue
                    }
                } else if(i > data1.size - 1) {
                    if(data2[i] > 0){
                        return -1
                    }
                } else if (i > data2.size - 1){
                    if(data1[i] > 0){
                        return 1
                    }
                }
            }

            return 0
        }
    }
}