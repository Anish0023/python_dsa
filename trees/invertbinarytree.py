from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        root.left , root.right = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print("original tree inorder traversal:")
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=' ')
            inorder(node.right)
    inorder(root)
    print("\nInverted tree inorder traversal:")
    # Invert the binary tree
    inverted_root = obj.invertTree(root)
    # Function to print inorder traversal of the tree
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=' ')
            inorder(node.right)
    # Print the inverted tree
    inorder(inverted_root)