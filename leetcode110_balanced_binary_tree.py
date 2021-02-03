# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def getDepth(node: TreeNode) -> int:
            if node is None:
                return 0
            left, right = getDepth(node.left), getDepth(node.right)
            
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left,right)+1
        
        return getDepth(root) != -1
