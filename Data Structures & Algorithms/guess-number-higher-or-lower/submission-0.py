# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low , high = 0 , n

        while True:
            g = (low + high )//2 

            output = guess(g)

            if output == 0:
                return g
            elif output ==1:
                low = g+1
            else:
                high = g-1
            