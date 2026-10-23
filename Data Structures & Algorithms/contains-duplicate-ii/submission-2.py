class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l , r = 0 , 1
        i = 0
        seen = set()
        setsize = 0

        # while l<len(nums):
        #     if nums[l]==nums[r]:
        #         return True
        #     else:
        #         if abs(l-r)>k:
        #             r+=1
        #         else:
        #             l+=1
        # return False
        while i<len(nums):
            if nums[i] in seen:
                return True
            if setsize==k:
                seen.remove(nums[l])
                setsize-=1
                l+=1
            seen.add(nums[i])
            setsize+=1
            i+=1
        return False