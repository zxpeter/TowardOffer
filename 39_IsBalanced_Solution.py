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

