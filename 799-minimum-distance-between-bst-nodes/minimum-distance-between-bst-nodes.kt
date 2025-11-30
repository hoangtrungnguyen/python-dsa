/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 * var left: TreeNode? = null
 * var right: TreeNode? = null
 * }
 */
class Solution {
    
private var curMin = Int.MAX_VALUE

  fun minDiffInBST(root: TreeNode?): Int {
        val values = mutableListOf<Int>()
        
        // 1. Collect all nodes in sorted order using In-Order traversal
        inOrderTraversal(root, values)

        // 2. Find the minimum difference between adjacent values
        var minDiff = Int.MAX_VALUE
        for (i in 1 until values.size) {
            val diff = values[i] - values[i - 1]
            if (diff < minDiff) {
                minDiff = diff
            }
        }
        return minDiff
    }

    private fun inOrderTraversal(node: TreeNode?, values: MutableList<Int>) {
        if (node == null) {
            return
        }

        // Traverse Left
        inOrderTraversal(node.left, values)

        // Visit Node (LeetCode usually names the value property `val`)
        values.add(node.`val`)

        // Traverse Right
        inOrderTraversal(node.right, values)
    }



}