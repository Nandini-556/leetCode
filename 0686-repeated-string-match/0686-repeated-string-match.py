class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        repeated = a
        count = 1

        # Repeat until length >= b
        while len(repeated) < len(b):
            repeated += a
            count += 1

        # Check if b is a substring
        if b in repeated:
            return count

        # One extra repetition for overlap cases
        repeated += a

        if b in repeated:
            return count + 1

        return -1