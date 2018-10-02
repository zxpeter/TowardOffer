# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        current_level = []
        current_level.append(root)
        res = []
        while current_level:
            level_res = []
            next_level = []
            for current in current_level:
                level_res.append(current.val)
                if current.left:
                    next_level.append(current.left)
                if current.right:
                    next_level.append(current.right)
            res.append(level_res)
            current_level = next_level
        return res    
            
