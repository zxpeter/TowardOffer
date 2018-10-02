# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def _pathSum(root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: int
            """
            count = 0
            if not root:
                return 0
            if root.val == sum:
                count += 1
            count += _pathSum(root.left, sum-root.val)
            count += _pathSum(root.right, sum-root.val)
            return count

        return _pathSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        
        
        
