# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (left.val==right.val and 
                    dfs(left.left,right.right) and
                    dfs(left.right,right.left))
        return dfs(root.left,root.right)
if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a symmetric binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    # Check if the tree is symmetric
    result = obj.isSymmetric(root)
    print(result)  # Output: True    