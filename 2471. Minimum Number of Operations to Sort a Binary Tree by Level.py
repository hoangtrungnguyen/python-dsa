from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



    def __str__(self):
        # return f'val: {self.va}'
        return self._diagram(self)

    def _diagram(self, tree_node, top='', root='', bottom=''):
        if tree_node is None:
            return f'{root} null\n'

        if tree_node.left is None and tree_node.right is None:
            return f'{root} {tree_node.val}\n'

        a = self._diagram(
            tree_node.right,
            f'{top} ',
            f'{top}┌──',
            f'{top}│ ',
        )

        b = f'{root}{tree_node.val}\n'

        c = self._diagram(
            tree_node.left,
            f'{bottom}│ ',
            f'{bottom}└──',
            f'{bottom} ',
        )
        return f'{a}{b}{c}'

class Solution:
    # helper: swap.
    # store elements in each level into list[list[int]]
    # sort each array
    # count swap
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        levels = []
        level = []
        while len(stack) > 0:
            node = stack.pop(0)
            level.append(node)
            if len(stack) == 0:
                # for e in level:
                #     print(f'e {e}')
                level_data = list(map(lambda x: x.val, level))
                levels.append(level_data)
                print(f'level_data: {level_data}')
                while len(level) > 0:
                    level_node = level.pop(0)
                    if level_node.left:
                        stack.append(level_node.left)
                    if level_node.right:
                        stack.append(level_node.right)




        print(f'levels: {levels}')
        total_count = 0
        for level_data in levels:
            count = self.sort(level_data)
            print(f'after sorting: {level_data} count: {count}')
            total_count += count

        return total_count

    def sort(self, arr):
        n = len(arr)
        index_map = {val: i for i, val in enumerate(arr)}  # Map values to original indices
        sorted_arr = sorted(arr)  # Efficiently sort the values
        visited = [False] * n  # Keep track of visited indices to avoid cycles
        swaps = 0

        for i in range(n):
            if visited[i] or index_map[sorted_arr[i]] == i:
                continue  # Skip if already part of a sorted cycle or already in place

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index_map[sorted_arr[j]]  # Follow the cycle
                cycle_size += 1
            if cycle_size > 0:
                swaps += cycle_size - 1  # Number of swaps in a cycle is cycle_size -1

        return swaps

    def swap(self, arr, i, j):
        """Swaps two elements in a list."""
        arr[i], arr[j] = arr[j], arr[i]

def build_tree(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = build_tree(nums[:mid])
    root.right = build_tree(nums[mid+1:])
    return root

# nums = [1, 2, 3, 4, 7, 6, 5]
# root = build_tree(nums)
# print(root)
#
# res = Solution().minimumOperations(root)
# print(f'count: {res}')
#
# nums = [1,3,2,7,6,5,4]
# root = build_tree(nums)
# print(root)
#
# res = Solution().minimumOperations(root)
# print(f'count: {res}')


node = TreeNode(val=1)
node3 = TreeNode(val=3)
node7 = TreeNode(val=7)
node6 = TreeNode(val=6)

node3.left = node7
node3.right = node6

node5 = TreeNode(val=5)
node4 = TreeNode(val=4)
node2 = TreeNode(val=2)
node2.left = node5
node2.right= node4

node.left = node3
node.right = node2

res = Solution().minimumOperations(node)
print(f'res {res}')
