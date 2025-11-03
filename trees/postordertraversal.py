# Definition for a binary tree node.
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorder(self, root , l1):
        if root is None:
            return None
        else:
            self.postorder(root.left,l1)
            self.postorder(root.right,l1)
            l1.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l1 = []
        self.postorder(root,l1)
        return l1

if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a binary tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # Perform preorder traversal
    result = obj.postorderTraversal(root)
    print(result)  
    