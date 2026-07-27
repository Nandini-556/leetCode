class Solution:
    def shuffle(self, nums, n):
        return [num for i in range(n) for num in (nums[i], nums[i+n])]