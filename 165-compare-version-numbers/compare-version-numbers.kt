class Solution {
    fun compareVersion(version1: String, version2: String): Int {
        var p1 = 0
        var p2 = 0

        while (p1 < version1.length || p2 < version2.length) {
            val (num1, nextP1) = getNextChunk(version1, p1)
            val (num2, nextP2) = getNextChunk(version2, p2)
            
            if (num1 < num2) {
                return -1
            } else if (num1 > num2) {
                return 1
            }
            
            p1 = nextP1
            p2 = nextP2
        }

        return 0
    }

    private fun getNextChunk(version: String, p: Int): Pair<Int, Int> {
        if (p >= version.length) {
            return Pair(0, p)
        }

        var end = p
        while (end < version.length && version[end] != '.') {
            end += 1
        }

        val num = if (p < end) version.substring(p, end).toInt() else 0
        val nextP = end + 1

        return Pair(num, nextP)
    }
}