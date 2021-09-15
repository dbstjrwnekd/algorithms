# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val: int = 0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return
        
        if root.val < low:
            self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            self.rangeSumBST(root.left, low, high)
        else:
            self.val += root.val
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
        
        return self.val
        