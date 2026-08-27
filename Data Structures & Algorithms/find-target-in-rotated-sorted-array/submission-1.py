class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1

        while left<=right:
            mid = left+ (right-left)//2

            if nums[mid]==target:
                return mid
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right = mid -1
                else:
                    left = left+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=left+1
                else:
                    right = right -1

        return -1