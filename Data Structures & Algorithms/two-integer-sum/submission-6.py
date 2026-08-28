class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            compval = target-nums[i]

            if compval in s:
                return [s[compval],i]
            else:
                s[nums[i]] = i