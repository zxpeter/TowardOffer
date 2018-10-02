class Solution:
    def IsBalanced(self, pRoot, depth):
        if pRoot is None:
            depth = 0
            return True
        if self.IsBalanced(pRoot.right, right) and self.IsBalanced(pRoot.left, left):
            diff = abs(left - right)
            if diff <= 1:
                depth = max(left, right) +1
                return True
        return False
    def IsBalanced_Solution(self, pRoot):
        # write code here
        depth = 0
        return self.IsBalanced(pRoot, depth)

if __name__ == '__main__':
    sol = Solution()
    sol.IsBalanced_Solution()

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(right-left) > 1:
                return -1
            return 1 + max(left, right)
        
        return check(root) != -1
        
