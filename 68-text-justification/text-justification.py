from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            line_length = len(words[i])
            j = i + 1

            # Greedily fit as many words as possible
            while j < n and line_length + 1 + len(words[j]) <= maxWidth:
                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            is_last_line = j == n

            # Last line or single word: left-justify
            if is_last_line or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                total_chars = sum(len(word) for word in line_words)
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces_per_gap + (1 if k < extra_spaces else 0))
                line += line_words[-1]

            result.append(line)
            i = j

        return result
