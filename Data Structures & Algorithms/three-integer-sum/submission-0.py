class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i==j or j==k or i==k: continue
                    if nums[i]+nums[j]+nums[k]==0:
                        soln.append([nums[i],nums[k],nums[j]])
        return soln