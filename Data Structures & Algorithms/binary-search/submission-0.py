class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low , high = 0, len(nums)
        
        while low<high:
            m = (low+high)//2

            if nums[m]==target:
                return m
            elif nums[m]<target:
                low = m+1
            else:
                high = m-1
        
        return -1