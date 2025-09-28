import kotlin.math.atan2
import kotlin.math.PI
import kotlin.math.abs

class Solution {
    fun largestTriangleArea(points: Array<IntArray>): Double {
//        println("points: ${points.map { "(${it[0]}, ${it[1]})" }.joinToString(", ")}")
        // S = h * d / 2 
        val sortedPoints = points.sortedWith { a, b ->
            val comparedX = a[0].compareTo(b[0])
            if (comparedX != 0) {
                comparedX
            } else {
                a[1].compareTo(b[1])
            }
        }

        // println("sortedPoints: ${sortedPoints.map { "(${it[0]}, ${it[1]})" }.joinToString(", ")}")

        val anchor = sortedPoints.first()

        val sortByAngleInDegrees = sortedPoints.filter {
            !anchor.contentEquals(it)
        }.sortedWith { a, b ->


            val ADegree = calculateAngleInDegrees(anchor, a)
            val BDegree = calculateAngleInDegrees(anchor, b)

            if (ADegree == BDegree) {
                if (b[0].compareTo(a[0]) == 0) {
                    b[1].compareTo(a[1])
                } else {
                    -b[0].compareTo(a[0])
                }
            } else {
                ADegree.compareTo(BDegree)
            }
        }


        // println("sortByAngleInDegrees: ${sortByAngleInDegrees.map { "(${it[0]}, ${it[1]})" }.joinToString(", ")}")


        val pointStack = Stack<IntArray>()

        pointStack.push(sortedPoints.first())


        for (i in 0 until sortByAngleInDegrees.size) {
            val C = sortByAngleInDegrees[i]
            if (pointStack.size == 1) {
                pointStack.push(C)
            } else {
                // if is left turn:
                //      push point to stack
                // else if is right turn:
                //      pop
                //      push point


                val A = pointStack.elements[pointStack.size - 2]
                val B = pointStack.elements.last()

                // AB formula
                // if A < Ox:
                //
                // else if A > Ox
                // if C
                if  (checkLeftTurn(A,B,C )){
                    pointStack.push(C)
                } else {
                    pointStack.pop()
                    pointStack.push(C)
                }
            }
        }

        var largestArea = 0.0

        // find the largest area
        val points = pointStack.elements
        for (i in 0 until pointStack.size - 1) {
            val A = points[i]

            for (j in 0 until pointStack.size) {
                if (j == i) {
                    continue
                }
                val B = points[j]

                for (k in j + 1 until points.size) {
                    val C = points[k]
                    val area = calculateArea(arrayOf<IntArray>(A, B, C))
                    if (area > largestArea) {
                        largestArea = area
                    }
                }
            }
        }


        // println("pointStack: ${pointStack.elements.map { "(${it[0]}, ${it[1]})" }.joinToString(", ")}")

        return largestArea
    }

    private fun calculateArea(points: Array<IntArray>): Double {
        val p1 = points[0]
        val p2 = points[1]
        val p3 = points[2]
//        println("Poinst: (${p1[0]}, ${p1[1]}) - (${p2[0]}, ${p2[1]}) - (${p3[0]}, ${p3[1]})")
        val area = 0.5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
//        println("calculateArea ${area}")
        return area
    }

    private fun calculateAngleInDegrees(p0: IntArray, cur: IntArray): Double {
        val deltaX = cur[0] - p0[0]
        val deltaY = cur[1] - p0[1]

        val angleInRadians = atan2(deltaY.toDouble(), deltaX.toDouble())
        val angleInDegrees = angleInRadians * (180 / PI)
//        println("p0: (${p0[0]}, ${p0[1]})")
//        println("cur: (${cur[0]}, ${cur[1]})")
//        println("angleInRadians: $angleInRadians")

        return angleInDegrees
    }

    private fun checkLeftTurn(p1: IntArray, p2: IntArray, p3: IntArray): Boolean{
       val value = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        return value > 0
    }
    inner class Stack<T> {
        val elements = ArrayDeque<T>()

        fun push(item: T) {
            size += 1
            elements.addLast(item) // Add to the end (top of the stack)
        }

        fun pop(): T? {
            size -= 1
            return elements.removeLastOrNull() // Remove from the end (top of the stack)
        }

        fun peek(): T? {
            return elements.lastOrNull() // Get the last element without removing
        }

        fun isEmpty(): Boolean {
            return elements.isEmpty()
        }

        var size: Int = 0
            private set
    }
}