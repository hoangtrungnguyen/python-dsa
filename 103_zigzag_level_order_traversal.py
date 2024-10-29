from typing import Optional
from typing import List




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# using recursive style
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        level: int -> store the current level. += 1 when move to the next level.
        result: List[List[int]] -> store values in each level
        for level
         level_values
         if level % 2 == 0:
            add from right to left to a level_values
            add the list to the result[level] += level_values
         elif level % 2 == 1 add from left to right
             add the list to the result[level] += level_values
        :param root:
        :return:
        """

        # time complexity: O(H)
        height = self.height(root)
        result = [ [] for _ in range(height)]
        # print(f'result: {result}')

        # time complexity: O(N x H)
        # N : Number of node in each level -> insert(0, value)
        # H : Height of the tree
        self.bread_first_search(root, 0, result)
        print(result)
        return result

    def height(self, root: Optional[TreeNode]) -> int:
        def _helper(root: Optional[TreeNode], count: int) -> int:
            if root is None:
                return count
            return max(_helper(root.left, count + 1), _helper(root.right, count + 1))
        return _helper(root, 0)



    def bread_first_search(self, root: Optional[TreeNode], level: int, list: List[List[int]]):
        if root is None:
            print(f'list.length: {len(list)}')
            return

        level_values = list[level]
        if level % 2 == 1:
            level_values.insert(0, root.val)
            list[level] = level_values
        else:
            level_values.append( root.val)
            list[level] = level_values

        self.bread_first_search(root.left, level + 1 , list)
        # print(f'level: {level}, val {root.val}')
        self.bread_first_search(root.right, level + 1, list)



# Using while loop and a queue
class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        :param root:
        :return:
        """
        return []




from dsa.nodes.tree_node import array_to_tree

# root1 = array_to_tree([3,9,20,None,None,15,7])
#
# # Solution().zigzagLevelOrder(root1)
# # print(f'expect: [[3],[20,9],[15,7]] - actual: {Solution().zigzagLevelOrder(root1)}')
#
#
# root2 = array_to_tree([1])
# # print(f'expect: [[1]] - actual: {Solution().zigzagLevelOrder(root2)}')
#
# # h = Solution().height(root1)
# # print(f'height: {h}')
#
# root3 = array_to_tree([])
# print(f'expect: [] - actual: {Solution().zigzagLevelOrder(root3)}')


root4 = array_to_tree([3,9,20,None,None,15,7, None, 2, None, 8, 2, 4, 5,12])
print(array_to_tree(root4))

