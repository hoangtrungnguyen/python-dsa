"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, input: Optional['Node']) -> Optional['Node']:
        visited = {} # map keys: old_node . values: new_node
        def dfs(node: Optional['Node']):
            if node in visited:
                return visited[node]
            if node is None:
                return node
            visited[node] = Node(node.val)
            children = []
            for child in node.neighbors:
                children.append(dfs(child))
            visited[node].neighbors = children
            return visited[node]

        return dfs(input)

        