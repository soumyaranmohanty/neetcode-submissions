class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(', '{', '[']
        clo = {')' : '(', 
                '}': '{', 
                ']': '['
                }

        stack = []
        pop_op =False
        if len(s)<2:
            return False

        for i in range(0,len(s)):
            if s[i] in op:
                stack.append(s[i])                
            if (s[i] in clo): 
                if (len(stack)!=0):
                    #check stack top element
                    if stack[-1]==clo[s[i]]:
                        stack.pop()
                        pop_op = True
                    else:
                        return False
                else:
                    return False
        if len(stack)==0 and pop_op:
            return True
        else:
            return False


        