class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        ans = 0 
        while(left<right):
            container = min(heights[left],heights[right]) * (right-left)
            ans = max(ans, container)

            if(heights[left]<heights[right]):
                left = left+1
            else:
                right = right - 1

        return ans