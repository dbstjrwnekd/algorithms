# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            new_node = TreeNode(t1.val + t2.val)
            new_node.left = self.mergeTrees(t1.left, t2.left)
            new_node.right = self.mergeTrees(t1.right, t2.right)
            return new_node
        else:
            return t1 or t2
        