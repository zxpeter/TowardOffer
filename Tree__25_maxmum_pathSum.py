# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        self._maxPathSum(root)
        return self.maxSum

    def _maxPathSum(self, root):  # DFS
        if root is None:
            return 0
        left = self._maxPathSum(root.left)
        right = self._maxPathSum(root.right)
        left = max(left, 0)
        right = max(right,0)
        self.maxSum = max(self.maxSum, root.val + left + right)
        # print self.maxSum
        return max(left, right) + root.val
