from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1 + self.minDepth(root.right)
        if root.right == None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
    
if __name__ == "__main__":    
    # Example usage:
    # Constructing a binary tree:
    #         1
    #        / \
    #       2   3
    #      /
    #     4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    obj = Solution()
    min_depth = obj.minDepth(root)
    print("Minimum Depth of the tree:", min_depth)  # Output: Minimum Depth of the tree: 2