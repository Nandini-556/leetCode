class Solution:
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                # We are on the increasing side
                left = mid + 1
            else:
                # We are on the decreasing side
                right = mid

        return left