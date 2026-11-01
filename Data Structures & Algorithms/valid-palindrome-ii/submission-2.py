class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(l , r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
            
        if is_pali(0 , len(s)-1):
            return True
        else:
            l = 0 
            r = len(s)-1

            while l<r:
                if s[l]!=s[r]:
                    return is_pali(l+1 , r) or is_pali(l, r-1)
                else:
                    l+=1
                    r-=1
            