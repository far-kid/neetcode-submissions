class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = int(a , 2)
        d = c + int(b , 2)
        return bin(d)[2:]