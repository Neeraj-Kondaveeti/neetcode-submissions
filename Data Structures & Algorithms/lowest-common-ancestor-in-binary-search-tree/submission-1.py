# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result = [root]

        def search(root):
            if not root:return 
            result[0] = root
            if p is root or q is root : return 
            elif root.val<p.val and root.val<q.val:
                search(root.right)
            elif root.val>p.val and root.val>q.val:
                search(root.left)

            else:
                return 
            
        search(root)
        return result[0]