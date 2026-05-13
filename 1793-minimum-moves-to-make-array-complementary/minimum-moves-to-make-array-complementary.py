class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        diff = [0] * (2 * limit + 2)

        n = len(nums)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # default: 2 moves
            diff[2] += 2

            # 1 move for sums in [low, high]
            diff[low] -= 1
            diff[high + 1] += 1

            # 0 moves for sum == s
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        cur = 0
        for target in range(2, 2 * limit + 1):
            cur += diff[target]
            ans = min(ans, cur)

        return ans
