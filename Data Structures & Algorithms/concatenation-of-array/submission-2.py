class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums)*2)
        len_n = len(nums)
        for i in range(len(ans)):
            if i<=len(nums)-1:
                ans[i]=nums[i]
            else:
                ans[i] = nums[i - len_n]
        return ans