from collections import deque
from typing import List


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        LOG = n.bit_length()
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        cnt = [[0] * 27 for _ in range(n)]  # weights are 1..26

        # BFS/DFS from root 0 to fill depth, parent[0], and prefix counts
        q = deque([0])
        seen = [False] * n
        seen[0] = True

        while q:
            u = q.popleft()
            for v, w in graph[u]:
                if seen[v]:
                    continue
                seen[v] = True
                depth[v] = depth[u] + 1
                parent[0][v] = u
                cnt[v] = cnt[u][:]      # copy prefix counts from parent
                cnt[v][w] += 1          # include edge (u, v)
                q.append(v)

        # Binary lifting table
        for k in range(1, LOG):
            for v in range(n):
                mid = parent[k - 1][v]
                if mid != -1:
                    parent[k][v] = parent[k - 1][mid]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for k in range(LOG):
                if diff & (1 << k):
                    a = parent[k][a]

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if parent[k][a] != parent[k][b]:
                    a = parent[k][a]
                    b = parent[k][b]

            return parent[0][a]

        ans = []
        for a, b in queries:
            c = lca(a, b)
            path_len = depth[a] + depth[b] - 2 * depth[c]

            best = 0
            for w in range(1, 27):
                freq = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w]
                best = max(best, freq)

            ans.append(path_len - best)

        return ans
