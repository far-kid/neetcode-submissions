class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if seen.get(i) is None:
                seen[i] = True
            else:
                return True
        return False