# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDepth = 0
    def dfs(self, node):
        if not node:
            return 0
            
        return max(self.dfs(node.left), self.dfs(node.right)) + 1
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return
        
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        self.maxDepth = max(self.maxDepth, self.dfs(root.left)+self.dfs(root.right))
        
        
        return self.maxDepth
            