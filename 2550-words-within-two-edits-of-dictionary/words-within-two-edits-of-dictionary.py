from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []

        for query in queries:
            for word in dictionary:
                diff = 0

                for i in range(len(query)):
                    if query[i] != word[i]:
                        diff += 1
                    if diff > 2:
                        break

                if diff <= 2:
                    result.append(query)
                    break

        return result
