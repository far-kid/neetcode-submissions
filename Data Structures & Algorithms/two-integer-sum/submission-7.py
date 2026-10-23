class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i , n in enumerate(nums):
            hashmap[n]= i

        for i in nums:
            if target-i in hashmap:
                return [min(hashmap[i] , hashmap[target-i]) , max(hashmap[i] , hashmap[target-i])]
    