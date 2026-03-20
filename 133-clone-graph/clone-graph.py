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
        if node is None:
            return None
        self.visited = {}
        return self._clone(node)

    def _clone(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        if node in self.visited:
            return self.visited[node]

        newNode = Node(val = node.val)
        self.visited[node] = newNode

        for e in node.neighbors:
            cloneNode = self._clone(e)
            newNode.neighbors.append(cloneNode)
        
        return newNode

        