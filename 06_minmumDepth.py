# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nleft = self.minDepth(root.left)
        nright = self.minDepth(root.right)
        if nleft == 0 or nright == 0:
            return nleft + nright + 1
        return min(nleft, nright) + 1
