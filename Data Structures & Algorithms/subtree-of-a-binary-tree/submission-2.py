# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root,subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            if root.val!= subroot.val:
                return False

            return sametree(root.left, subroot.left) and sametree(root.right, subroot.right)

        def hassubtree(root):
            if not root:return False
            if sametree(root,subRoot):
                return True
            return hassubtree(root.left) or hassubtree(root.right)

        return hassubtree(root)