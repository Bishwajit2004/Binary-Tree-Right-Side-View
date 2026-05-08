from collections import deque, defaultdict
from math import isqrt

class Solution:
    def minJumps(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        # Smallest prime factor sieve
        spf = list(range(max_val + 1))
        for i in range(2, isqrt(max_val) + 1):
            if spf[i] == i:
                for j in range(i * i, max_val + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_prime_factors(x: int) -> list[int]:
            factors = []
            while x > 1:
                p = spf[x]
                factors.append(p)
                while x % p == 0:
                    x //= p
            return factors

        def is_prime(x: int) -> bool:
            return x >= 2 and spf[x] == x

        # prime -> all indices whose nums[idx] is divisible by prime
        prime_to_indices = defaultdict(list)
        for i, x in enumerate(nums):
            for p in get_prime_factors(x):
                prime_to_indices[p].append(i)

        dist = [-1] * n
        dist[0] = 0
        q = deque([0])

        used_prime = set()

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            # adjacent moves
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = d + 1
                q.append(i - 1)

            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = d + 1
                q.append(i + 1)

            # teleport moves
            val = nums[i]
            if is_prime(val) and val not in used_prime:
                for nxt in prime_to_indices[val]:
                    if dist[nxt] == -1:
                        dist[nxt] = d + 1
                        q.append(nxt)
                used_prime.add(val)

        return -1
