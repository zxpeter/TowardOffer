# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack1 = []        
        self.stack2 = []

        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.stack1.append(root.val)
        if root.left or root.right:
            self.pathSum(root.left, sum-root.val)
            self.pathSum(root.right, sum-root.val)
        else:
            if root.val == sum:
                self.stack2.append(list(self.stack1))
                print(list(self.stack1))
        self.stack1.pop()
        return self.stack2
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.stack1.append(root.val)
        if root.left or root.right:
            self.binaryTreePaths(root.left)
            self.binaryTreePaths(root.right)
        else:
            a = [str(i) for i in list(self.stack1)]
            res = '->'.join(a)
            self.stack2.append(res)
            # print(list(self.stack1))
        self.stack1.pop()
        return self.stack2
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.stack = []
        self.sum = 0
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.stack.append(root.val)
        if root.left or root.right:
            self.sumNumbers(root.left)
            self.sumNumbers(root.right)
        else:
            a = [str(i) for i in list(self.stack)]
            b = int(''.join(a))
            self.sum += b
            
        self.stack.pop()
        return self.sum
