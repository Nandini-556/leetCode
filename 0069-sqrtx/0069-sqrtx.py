class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        left = 1
        right = x
        answer = 0

        while left <= right:
            middle = (left + right) // 2
            square = middle * middle

            if square == x:
                return middle

            if square < x:
                answer = middle
                left = middle + 1
            else:
                right = middle - 1

        return answer