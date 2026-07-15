class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for number in arr:
            if (2 * number) in seen:
                return True

            if number % 2 == 0 and (number // 2) in seen:
                return True

            seen.add(number)

        return False