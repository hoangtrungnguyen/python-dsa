# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # path = ""
        result = []

        def dfs(node:Optional[TreeNode], path: str):
            if node is None:
                result.append(path)
                return 
            # print(node.val)
            # path = f""
            # result.append(path)
            # if node.left is None and node.right is None:
            #     path = ""
            # print(f"path {path}")

            
            if path == '':
                path = f'{node.val}'
            else:
                path = f'{path}->{node.val}'

            if node.left:
                left_path = dfs(node.left, path)
                if left_path:
                    path = f"{left_path}->{path}"
                
            if node.right:
                right_path = dfs(node.right, path)
                if right_path:
                    path = f"{right_path}->{path}"

            # print(f'path: {path}')
            if node.left is None and node.right is None:
                # print(f"path at leaf: {path}")
                result.append(path)

                # path = f'{node.val}'

        dfs(root, "")
        return result
        