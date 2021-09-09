# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -float('inf')
    minDiff = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        
        if root.left:
            self.minDiffInBST(root.left)
            
        self.minDiff = min(self.minDiff, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.minDiff
        