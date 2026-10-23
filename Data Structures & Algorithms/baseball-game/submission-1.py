from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        result = 0

        for i in operations:
            if i == '+':
                stack.append(stack[-1]+stack[-2])
                result+=stack[-1]
            elif i== 'D':
                stack.append(stack[-1]*2)
                result+=stack[-1]
            elif i=='C':
                result-=stack.pop()
            else:
                stack.append(int(i))
                result+=int(i)
            print(stack)
            
        return result
