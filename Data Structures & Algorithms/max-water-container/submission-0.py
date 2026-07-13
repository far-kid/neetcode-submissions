class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        for i in range(len(heights)):
            for j in range(i , len(heights)):
                newvol = min(heights[i], heights[j]) * (j-i)
                vol = max(vol , newvol)
        return vol