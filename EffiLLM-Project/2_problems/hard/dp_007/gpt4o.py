from typing import List

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {}
        for i, c in enumerate(s):
            if c not in index:
                index[c] = [-1]
            index[c].append(i)
        for c in index:
            index[c].append(len(s))
        res = 0
        for arr in index.values():
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res
