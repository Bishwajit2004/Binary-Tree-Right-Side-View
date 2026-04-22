from typing import List
from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        word_count = defaultdict(int)

        for message, sender in zip(messages, senders):
            word_count[sender] += len(message.split())

        best_sender = ""
        best_count = 0

        for sender, count in word_count.items():
            if count > best_count or (count == best_count and sender > best_sender):
                best_count = count
                best_sender = sender

        return best_sender
