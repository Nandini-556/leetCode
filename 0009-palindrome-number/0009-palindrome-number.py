class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10

        return original_number == reversed_number