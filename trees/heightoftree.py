from typing import Optional
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)

if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    obj = Solution()
    height = obj.maxDepth(root)
    print("Height of the tree:", height)  # Output: Height of the tree: 3
        