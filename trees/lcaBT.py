# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right
        '''
        Base case: If root is null, return null.
If root is equal to either p or q, return root.
Recursively check left and right subtree.
If both return non-null, current node is the LCA.
If only one is non-null, propagate it upward.
        
        '''

if __name__ == "__main__":
    # Example usage:
    # Constructing a binary tree:
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4
    root = TreeNode(3)
    p = TreeNode(5)
    q = TreeNode(1)
    root.left = p
    root.right = q
    p.left = TreeNode(6)
    p.right = TreeNode(2)
    p.right.left = TreeNode(7)
    p.right.right = TreeNode(4)
    q.left = TreeNode(0)
    q.right = TreeNode(8)

    obj = Solution()
    lca = obj.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.val)  # Output: Lowest Common Ancestor: 3