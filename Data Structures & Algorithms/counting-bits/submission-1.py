class Solution:
    def countBits(self, n: int) -> List[int]:
        def co(t):
            c = 0
            while t:
                t &= t - 1
                c+=1
            return c
        arr = []

        for i in range(n+1):
            arr.append(co(i))
        return arr