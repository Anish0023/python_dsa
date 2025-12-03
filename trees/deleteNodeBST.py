# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMin(self,root):
        while root.left != None:
            root = root.left
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            # with no child
            if root.left == None and root.right == None:
                return None
            # node with only one child
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            #  node with two child : get the inorder successor (smallest in right sub tree)
            tmp = self.findMin(root.right)
            root.val = tmp.val
            root.right = self.deleteNode(root.right,tmp.val)
        return root
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)  
    key = 3
    new_root = s.deleteNode(root, key)
    # Function to print inorder traversal of the tree
    def inorder(root):
        if root:
            inorder(root.left)
            print(root.val, end=' ')
            inorder(root.right)
    inorder(new_root)  # Output: 2 4 5 6 7

            
        
        