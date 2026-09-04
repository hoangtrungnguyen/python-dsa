"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = {
            node: Node(node.val)
        }
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nb in cur.neighbors:
                if nb not in visited:
                    visited[nb] = Node(nb.val)
                    queue.append(nb)

                visited[cur].neighbors.append(visited[nb]) # use new node, which is value 
                    
        return visited[node]