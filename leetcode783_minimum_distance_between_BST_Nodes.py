# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        
        if root.right:
            step = root.right
            while step.left:
                step = step.left
            self.val = min(self.val, step.val-root.val)
        
        if root.left:
            step = root.left
            while step.right:
                step = step.right
            self.val = min(self.val, root.val-step.val)
        
        self.minDiffInBST(root.left)
        self.minDiffInBST(root.right)
        
        return self.val
        