class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        good_pairs = 0

        for number in nums:
            good_pairs += frequency.get(number, 0)
            frequency[number] = frequency.get(number, 0) + 1

        return good_pairs