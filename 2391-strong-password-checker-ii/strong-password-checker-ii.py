class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        specials = set("!@#$%^&*()-+")
        has_lower = has_upper = has_digit = has_special = False

        for i, ch in enumerate(password):
            if i > 0 and password[i] == password[i - 1]:
                return False

            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in specials:
                has_special = True

        return has_lower and has_upper and has_digit and has_special
