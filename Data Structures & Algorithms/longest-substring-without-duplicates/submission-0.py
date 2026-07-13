class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0,0
        newset = set()
        m_len = 0
        for r in range(len(s)):
            while s[r] in newset:
                newset.remove(s[l])
                l+=1
            newset.add(s[r])
            m_len = max(m_len , r-l+1)
        return m_len