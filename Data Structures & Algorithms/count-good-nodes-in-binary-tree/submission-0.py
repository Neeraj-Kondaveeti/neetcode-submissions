# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max1):
            if not node: return 0

            good =1 if node.val>=max1 else 0 

            max2 = max(max1,node.val)

            left = dfs(node.left,max2)
            right = dfs(node.right,max2)

            return good+left+right
        return dfs(root,root.val)