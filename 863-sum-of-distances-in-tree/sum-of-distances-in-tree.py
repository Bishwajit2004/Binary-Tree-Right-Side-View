class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        count = [1] * n
        answer = [0] * n

        def dfs1(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue

                dfs1(nei, node)

                count[node] += count[nei]
                answer[node] += answer[nei] + count[nei]

        def dfs2(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue

                answer[nei] = answer[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return answer
