class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l =0
        max_len = 0
        for i in s:
            if i in seen:
                while i in seen:
                    seen.remove(s[l])
                    l+=1
            
            seen.add(i)
            max_len = max(max_len , len(seen))

        return max_len