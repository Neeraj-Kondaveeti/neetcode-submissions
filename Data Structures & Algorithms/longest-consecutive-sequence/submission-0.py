class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        lval = 0 
        for num in numset:
            if num -1 not in numset:
                current = num
                le = 1 
                while current + 1 in numset:
                    current = current + 1 
                    le = le + 1 
                lval = max(le, lval)
        return lval