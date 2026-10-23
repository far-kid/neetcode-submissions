class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        k = 0
        maxm = 0
        j = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1

            seen.add(s[i])
            maxm = max(maxm, i - j + 1)

        return maxm