class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = set()
        tMap = set()
        for _ in s:
            sMap.add(_)
        for _ in t:
            tMap.add(_)
        if sMap == tMap:
            return True
        else:
            return False
        