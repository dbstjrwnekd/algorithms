# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth, step = [0], root
        def findDepth(node: TreeNode,depth: int):
            if not node.left and not node.right:
                max_depth[0] = max(max_depth[0],depth)
                return
            if node.left:
                findDepth(node.left,depth+1)
            if node.right:
                findDepth(node.right,depth+1)
        findDepth(step, 1)
        return max_depth[0]