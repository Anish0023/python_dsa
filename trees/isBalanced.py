from typing import Optional
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def isBalanced(self,root:Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return [True,0] #balanced,height
            left_balanced,left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return [is_balanced, 1 + max(left_height, right_height)]
        return dfs(root)[0]
    
if __name__ == "__main__":
    obj = Solution()
    # Constructing a balanced binary tree:
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
    balanced = obj.isBalanced(root)
    print("Is the tree balanced?", balanced)  # Output: Is the tree balanced? True  