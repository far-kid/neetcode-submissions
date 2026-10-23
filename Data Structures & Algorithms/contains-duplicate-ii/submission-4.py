class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k ==0:
            return False
        seen = set()
        i = 0
        for n in nums:
            if n in seen:
                return True
            if len(seen)==k and len(seen)!=0:
                seen.remove(nums[i])
                i+=1
            seen.add(n)
        return False
        
        