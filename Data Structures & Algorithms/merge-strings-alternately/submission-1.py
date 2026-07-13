class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_p , w2_p = 0,0
        newstr = ''

        while w1_p<len(word1) or w2_p<len(word2):
            if w1_p<len(word1):
                newstr+=word1[w1_p]
                w1_p+=1
            if w2_p<len(word2):
                newstr+=word2[w2_p]
                w2_p+=1
        
        return newstr