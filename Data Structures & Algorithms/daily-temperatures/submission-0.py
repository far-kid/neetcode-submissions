class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = []
        tem = temperatures
        n = len(temperatures)
        for i in range(n):
            count = 1
            j = i+1
            while j<n:
                if tem[j]>tem[i]:
                    break
                j+=1
                count+=1
            count = 0 if j==n else count
            r.append(count)
        return r