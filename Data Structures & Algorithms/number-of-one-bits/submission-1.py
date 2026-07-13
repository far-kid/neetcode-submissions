class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        if n%2==1:
            count +=1

        while n!=0:
            n = n>>1
            if n%2==1:
                count+=1
        return count