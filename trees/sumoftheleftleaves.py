# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def inorder(root, is_left):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            return inorder(root.left,True) + inorder(root.right,False)
        return inorder(root,False)
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)  
    print(s.sumOfLeftLeaves(root))  # Output: 24
   # Output: 11
