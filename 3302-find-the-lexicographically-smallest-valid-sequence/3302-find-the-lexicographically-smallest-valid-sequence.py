class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # suf[i] = maximum number of characters from the
        # suffix of word2 that can be matched using word1[i:]
        suf = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1]

            j = m - suf[i + 1] - 1

            if j >= 0 and word1[i] == word2[j]:
                suf[i] += 1

        ans = []
        used = False
        p = 0

        for i in range(n):
            if p == m:
                break

            # Exact match
            if word1[i] == word2[p]:
                ans.append(i)
                p += 1

            # Use the one allowed mismatch
            elif not used:
                need = m - (p + 1)

                if suf[i + 1] >= need:
                    ans.append(i)
                    p += 1
                    used = True

        return ans if p == m else []