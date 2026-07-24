class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2
            square = middle * middle

            if square == num:
                return True
            elif square < num:
                left = middle + 1
            else:
                right = middle - 1

        return False