class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_b = ['[' , '{' , '(']
        for i in s:
            if i in open_b:
                stack.append(i)
            elif i == ']':
                if len(stack)==0 or stack[-1]!='[':
                    return False
                else:
                    stack.pop()
            elif i =='}':
                if len(stack)==0 or stack[-1]!='{':
                    return False
                else:
                    stack.pop()
            else:
                if len(stack)==0 or stack[-1]!='(':
                    return False
                else:
                    stack.pop()
        return True if len(stack)==0 else False
