import collections

CAP = 10**6 + 1  # anything at/above this counts as "more than any possible k"

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = collections.Counter(s)

        # A palindrome rearrangement exists iff at most one letter has odd count.
        if sum(1 for v in freq.values() if v & 1) > 1:
            return ""

        half = [0] * 26
        mid = ""
        for ch, f in freq.items():
            half[ord(ch) - 97] = f // 2
            if f & 1:
                mid = ch

        total = self._arrangements(half)
        if k > total:
            return ""

        left = []
        remaining = sum(half)
        for _ in range(remaining):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = self._arrangements(half)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half[i] += 1

        right = left[::-1]
        return "".join(left) + mid + "".join(right)

    @staticmethod
    def _arrangements(counts):
        """# of distinct permutations of the half-multiset, saturating at CAP."""
        n = sum(counts)
        result = 1
        for c in counts:
            if c == 0:
                continue
            result = Solution._choose(n, c) * result
            if result >= CAP:
                return CAP
            n -= c
        return result

    @staticmethod
    def _choose(n, r):
        """C(n, r), saturating early once it reaches CAP."""
        r = min(r, n - r)
        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) // i
            if res >= CAP:
                return CAP
        return res