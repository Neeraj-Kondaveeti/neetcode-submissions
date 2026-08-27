class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        low = 0
        high = total-1
        while low<=high:
            mid = (low+high)//2
            i = mid // cols
            j = mid % cols
            mid_num = matrix[i][j]
            if target==mid_num:
                return True
            elif target<mid_num:
                high = mid-1
            else:
                low = mid+1
        return False
