class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i , n in enumerate(nums):
            c = target - n

            if c in h and h[c]!=i:
                return [h[c] , i]
            h[n]=i