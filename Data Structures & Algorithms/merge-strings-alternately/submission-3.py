class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr= []

        for i in range(min(len(word1) , len(word2))):
            newstr.append(word1[i])
            newstr.append(word2[i])
        
        if len(word1)<len(word2):
            newstr += list(word2[i+1:])
        else:
            newstr+=list(word1[i+1:])
        
        return ''.join(newstr)