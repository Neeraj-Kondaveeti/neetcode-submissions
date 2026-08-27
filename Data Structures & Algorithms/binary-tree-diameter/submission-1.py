
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_diameter = 0 

        def height(root):

            if not root: return 0 

            left = height(root.left)
            right = height(root.right)

            self.largest_diameter = max(self.largest_diameter, left+right)

            return 1+max(left,right)

        height(root)

        return self.largest_diameter
            
