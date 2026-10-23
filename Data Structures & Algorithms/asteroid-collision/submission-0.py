class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if s and i * s[-1] < 0:
                if abs(i)==abs(s[-1]):
                    s.pop()
                    continue
                if abs(i) < abs(s[-1]):
                    continue
                else:
                    while len(s)!=0 and abs(i) > abs(s[-1]) and i * s[-1] < 0:
                        s.pop()
                    s.append(i)
            else:
                s.append(i)
        return s