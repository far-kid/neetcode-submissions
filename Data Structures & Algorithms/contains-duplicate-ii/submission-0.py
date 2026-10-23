class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        seen = set()
        for n in nums:
            if n in seen:
                return True
            if len(seen)==k:
                seen.remove(nums[i])
                i+=1
            seen.add(n)
        return False