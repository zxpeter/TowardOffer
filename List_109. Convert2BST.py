# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        tree = []
        while head:
            tree.append(head.val)
            head = head.next
        root = self.constructTree(tree)        
        return root
    
    def constructTree(self, tree):
        if not tree:
            return
        mid = len(tree)/2
        root = TreeNode(tree[mid])
        root.left = self.constructTree(tree[:mid])
        root.right = self.constructTree(tree[mid+1:])
        return root
