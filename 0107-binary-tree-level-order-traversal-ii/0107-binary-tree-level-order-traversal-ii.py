# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            current_value = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_value.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            
            result.append(current_value)
            
        result.reverse()
        return result
                
                
        
        