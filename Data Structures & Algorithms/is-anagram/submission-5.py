class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_l = list(s)
        t_l = list(t)
        s_l.sort()
        t_l.sort()
        for i in range(len(s_l)):
            if s_l[i]!=t_l[i]:
                return False
        return True