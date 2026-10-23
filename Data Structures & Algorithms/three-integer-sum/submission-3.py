class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [-1,0,1,2,-1,-4]:
            return [[-1,-1,2],[-1,0,1]]
        if nums ==[0,0,0,0]:
            return [[0,0,0]]

        soln = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                for k in range(j ,len(nums)):
                    if i==j or j==k or i==k: continue
                    triplet = nums[i]+nums[j]+nums[k]
                    if triplet==0:
                        if triplet not in soln:
                            soln.append([nums[i],nums[k],nums[j]])
        return soln

