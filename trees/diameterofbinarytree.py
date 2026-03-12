# Definition for a binary tree node.
'''
Finding the diameter of a binary tree involves calculating 
the longest path between any two nodes in the tree. 
This path may or may not pass through the root. 
The diameter can be found by calculating the depth of the tree 
while keeping track of the longest path found at each node using the concept 
of finding the height of the tree.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def depth(self,root,maxi_dia):
        if not root:
            return (maxi_dia,0)
        maxi_dia, lh = self.depth(root.left , maxi_dia)
        maxi_dia, rh = self.depth(root.right, maxi_dia)
        node_dia = lh + rh
        maxi_dia = max(node_dia, maxi_dia)
        return (maxi_dia, 1 + max(lh,rh))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi_dia = 0
        ans  =  self.depth(root, maxi_dia)
        return ans[0]
if __name__=='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))