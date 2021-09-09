# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int  = 0
    def bstToGst(self, root: TreeNode, bigger=0) -> TreeNode:
        if not root:
            return
        self.bstToGst(root.right, bigger)
        value = root.val
        root.val += self.val
        self.val += value
        self.bstToGst(root.left, bigger)
        
        return root
        