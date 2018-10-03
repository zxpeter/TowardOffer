class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:

    def buildTree_pre_in(self, preorder, inorder):
        if inorder==[]:
            return None
        root = TreeNode(preorder[0])
        #print(preorder,inorder)
        x = inorder.index(root.val)#找到根在中序中的位置
        root.left=self.buildTree_pre_in(preorder[1:x+1],inorder[0:x])
        root.right=self.buildTree_pre_in(preorder[x+1:],inorder[x+1:])
        return root

    def buildTree_in_post(self, inorder, postorder):

        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        n = inorder.index(root.val)
        root.left = self.buildTree_in_post(inorder[:n], postorder[:n])
        root.right = self.buildTree_in_post(inorder[n + 1:], postorder[n:-1])
        return root

    def level_visit(self, root):
        queue = []
        if not root:
            return
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


if __name__ == '__main__':

    preorder = [1,2,4,7,3,5,6,8]
    inorder = [4,7,2,1,5,3,8,6]
    postorder = [7,4,2,5,8,6,3,1]
    sol = Tree()
    root = sol.buildTree_pre_in(preorder, inorder)
    sol.level_visit(root)
    print('----')
    root2 = sol.buildTree_in_post(inorder, postorder)
    sol.level_visit(root2)

