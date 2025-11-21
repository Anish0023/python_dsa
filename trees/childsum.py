from typing import Optional
# Definition for a binary tree node. this problem is to check  if the sum of the child nodes == root node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def childSum(self, root: Optional[TreeNode]) -> int:
        if root is None or (root.left is None and root.right is None):
            return 1
        if root.left:
            ldata = root.left.val # get left child data
        else:
            ldata = 0
        if root.right:
            rdata = root.right.val
        else:
            rdata = 0 
        if (root.val == ldata + rdata) and self.childSum(root.left) and self.childSum(root.right):
            
            return 1
        else:
            return 0
               