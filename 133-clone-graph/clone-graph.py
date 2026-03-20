"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def clone(node):
            if node in visited:
                return visited[node]
            
            visited[node] = Node(node.val)
            visited[node].neighbors = [clone(n) for n in node.neighbors]
            return visited[node]

        return clone(node) if node else None
        