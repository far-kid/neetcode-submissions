class Solution:
    def isPalindrome(self, s: str) -> bool:
        news =[]
        for i in s:
            if i.isalnum():
                news.append(i)
        news = ''.join(news)
        s = news.lower()
        i , j = 0 , len(s)-1
        print(s)
        while i < j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True