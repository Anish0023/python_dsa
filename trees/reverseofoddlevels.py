from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverse_tree(self,left_node,right_node , lvl):
        if not left_node or not right_node:
            return
        if lvl % 2 == 1:
            left_node.val, right_node.val = right_node.val, left_node.val

        self.reverse_tree(left_node.left, right_node.right, lvl + 1)
        self.reverse_tree(left_node.right, right_node.left, lvl + 1)
         
        
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # starting at level 1
        self.reverse_tree(root.left, root.right , 1)
        return root
    # Function to print the tree in level order for verification
    def print_tree(self, node):
        if not node:
            return []
        return [node.val] + self.print_tree(node.left) + self.print_tree(node.right)
    
if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Print the original tree in level order
    print(obj.print_tree(root))
    # Reverse odd levels
    result = obj.reverseOddLevels(root)
    
    # Function to print the tree in level order for verification

    print(obj.print_tree(result))  # Output the modified tree in level order
        
