class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = set()
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [nums.index(target-nums[i]), i ]
            else:
                if nums[i] not in hashmap:
                    hashmap.add(nums[i])