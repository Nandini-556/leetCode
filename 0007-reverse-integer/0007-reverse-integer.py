class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        reversed_number *= sign

        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0

        return reversed_number