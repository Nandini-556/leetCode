class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                # Target is on the right
                left = mid + 1

            else:
                # Target is on the left
                right = mid - 1

        return -1