from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, None, 0)])  # Initialize with a tuple (node, parent, depth)
        x_parent, x_depth, y_parent, y_depth = None, None, None, None
        
        while queue:
            node, parent, depth = queue.popleft()
            
            if node.val == x:
                x_parent, x_depth = parent, depth
            elif node.val == y:
                y_parent, y_depth = parent, depth
            
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
                
            # Early stopping condition if both nodes are found
            if x_parent is not None and y_parent is not None:
                break
        
        return (x_depth == y_depth) and (x_parent != y_parent)

