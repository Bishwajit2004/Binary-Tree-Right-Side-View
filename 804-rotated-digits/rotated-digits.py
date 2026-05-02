class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0
        changing = {'2', '5', '6', '9'}
        invalid = {'3', '4', '7'}

        for num in range(1, n + 1):
            s = str(num)
            has_change = False
            valid = True

            for ch in s:
                if ch in invalid:
                    valid = False
                    break
                if ch in changing:
                    has_change = True

            if valid and has_change:
                good += 1

        return good
