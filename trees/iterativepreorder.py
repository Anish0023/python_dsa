# Definition for a binary tree node.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
        return ans


if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a binary tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # Perform preorder traversal
    result = obj.preorderTraversal(root)
    print(result)  
    