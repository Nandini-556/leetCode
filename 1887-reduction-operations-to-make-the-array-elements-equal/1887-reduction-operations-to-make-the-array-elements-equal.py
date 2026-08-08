class Solution:
    def reductionOperations(self, nums):
        nums.sort()

        operations = 0
        greater = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                greater += 1

            operations += greater

        return operations     