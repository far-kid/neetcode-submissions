class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        i , j = 0, len(heights)-1
        h = heights

        while i<j:
            newvol = (j-i) * min(h[i] , h[j])

            vol = max(newvol , vol)

            if h[i]<h[j]:
                i+=1
            else: j-=1

        return vol