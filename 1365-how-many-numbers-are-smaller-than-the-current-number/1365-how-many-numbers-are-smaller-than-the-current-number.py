class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        count = {}

        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i

        result = []

        for num in nums:
            result.append(count[num])

        return result