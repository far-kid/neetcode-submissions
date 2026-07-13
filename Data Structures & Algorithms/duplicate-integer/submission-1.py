class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for _ in range(len(nums)-1):
            if nums[_]==nums[_+1]:
                return True
        return False
