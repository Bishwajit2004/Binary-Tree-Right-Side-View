from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        left = []

        for d in "9876543210":
            pairs = count[d] // 2
            if d == '0' and not left:
                continue
            if pairs > 0:
                left.append(d * pairs)
                count[d] -= pairs * 2

        left_half = "".join(left)

        middle = ""
        for d in "9876543210":
            if count[d] > 0:
                middle = d
                break

        if not left_half and middle:
            return middle

        return left_half + middle + left_half[::-1]
