from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        result = 0

        for i in operations:
            if i.isdigit():
                stack.append(int(i))
                result+=int(i)
            elif i == '+':
                stack.append(stack[-1]+stack[-2])
                result+=stack[-1]
            elif i== 'D':
                stack.append(stack[-1]*2)
                result+=stack[-1]
            else:
                result-=stack.pop()
            
        return result
