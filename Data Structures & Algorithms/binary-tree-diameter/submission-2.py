
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0] 

        def height(root):

            if not root: return 0 

            left = height(root.left)
            right = height(root.right)

            largest_diameter[0] = max(largest_diameter[0], left+right)

            return 1+max(left,right)

        height(root)

        return largest_diameter[0]
            
