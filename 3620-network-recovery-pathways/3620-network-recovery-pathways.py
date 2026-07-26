from typing import List
from heapq import heappush, heappop
from math import inf

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]

        lo = float('inf')
        hi = 0

        # Build graph using only online nodes
        for u, v, w in edges:
            if online[u] and online[v]:
                graph[u].append((v, w))
                lo = min(lo, w)
                hi = max(hi, w)

        if lo == float('inf'):
            return -1

        def check(mid):
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]

            while pq:
                d, u = heappop(pq)

                if d > k:
                    return False
                if u == n - 1:
                    return True
                if d > dist[u]:
                    continue

                for v, w in graph[u]:
                    if w < mid:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        left, right = lo, hi
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left if check(left) else -1