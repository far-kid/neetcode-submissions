class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_st1 = len(word1)
        len_st2 = len(word2)
        w1_p = 0
        w2_p = 0
        newstr = ''
        while len_st1>w1_p and len_st2>w2_p:
            newstr+=word1[w1_p]
            newstr+=word2[w2_p]
            w1_p+=1
            w2_p+=1
        
        if len_st1==w1_p and len_st2>w2_p:
            while len_st2>w2_p:
                newstr+=word2[w2_p]
                w2_p+=1
        if len_st2==w2_p and len_st1>w1_p:
            while len_st1>w1_p:
                newstr+=word1[w1_p]
                w1_p+=1
        return newstr