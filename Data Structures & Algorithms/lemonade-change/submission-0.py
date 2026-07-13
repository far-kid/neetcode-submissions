class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        left_5 = left_10 = 0

        for bill in bills:
            if bill==5:
                left_5+=1
            
            elif bill==10:
                if left_5>0:
                    left_5-=1
                    left_10+=1
                else:
                    return False
            
            else:
                if left_10>0 and left_5>0:
                    left_10-=1
                    left_5-=1

                else:
                    if left_5<3:
                        return False
                    else:
                        left_5-=3
        return True