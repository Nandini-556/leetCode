from collections import deque
from math import inf
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        q = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < m and 0 <= ny < n and
                        dist[nx][ny] > dist[x][y] + grid[nx][ny]):
                    dist[nx][ny] = dist[x][y] + grid[nx][ny]
                    q.append((nx, ny))

        return dist[m - 1][n - 1] < health