class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        h_s = {}
        t_s = {}

        for i in range(len(s)):
            h_s[s[i]] = h_s.get(s[i] , 0) + 1
            t_s[t[i]] = t_s.get(t[i] , 0) + 1
        
        return h_s == t_s