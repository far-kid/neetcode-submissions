# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0

        def dep(node):
            if not node:
                return 0
            left = dep(node.left)
            r = dep(node.right)
            self.d = max(self.d , left +r)
            return 1+ max(left , r)

        dep(root)
        return self.d