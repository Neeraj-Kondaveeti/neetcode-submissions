class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        leftprod = 1 
        for i in range(n):
            res[i] = leftprod
            leftprod = leftprod * nums[i]

        rightprod = 1 
        for j in range(n-1,-1,-1):
            res[j] = res[j] * rightprod
            rightprod = rightprod * nums[j]
        return res