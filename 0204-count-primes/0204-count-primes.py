class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        number = 2

        while number * number < n:
            if is_prime[number]:
                for multiple in range(number * number, n, number):
                    is_prime[multiple] = False
            number += 1

        count = 0

        for value in is_prime:
            if value:
                count += 1

        return count