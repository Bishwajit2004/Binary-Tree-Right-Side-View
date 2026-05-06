from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        cleaned = []

        for ch in paragraph.lower():
            if ch.isalpha():
                cleaned.append(ch)
            else:
                cleaned.append(' ')

        words = ''.join(cleaned).split()
        count = Counter(word for word in words if word not in banned_set)

        return count.most_common(1)[0][0]
