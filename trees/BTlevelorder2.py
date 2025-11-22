#  return the bottom up approach
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def level(self, root,lvl, ans):
        if root == None:
            return None
        if len(ans) <= lvl:
            ans.append([])
        ans[lvl].append(root.val)
        self.level(root.left, lvl + 1 , ans)
        self.level(root.right, lvl + 1 ,ans)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.level(root, 0 , ans)
        return ans[::-1]
    
if __name__ == "__main__":
    obj = Solution()
    # Example usage:
    # Construct a binary tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # Perform preorder traversal
    result = obj.levelOrder(root)
    print(result)
