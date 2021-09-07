# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return max(left,right) + 1
        
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        
        left = dfs(root.left)
        right = dfs(root.right)
        if abs(left-right) < 2:
            return True
        
        return False
        