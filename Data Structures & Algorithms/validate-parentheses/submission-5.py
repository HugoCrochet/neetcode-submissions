class Solution:
    def isValid(self, s: str) -> bool:
        
        close_to_open = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        
        stack = []
        l = len(s)
        i=0
        for char in s:
            i+=1
            print("iteration :", i, "/", l)
            print(stack)
            if char in close_to_open : 
                if len(stack) == 0 : 
                    return False
                print("stack[-1] : ", stack[-1])
                if close_to_open[char] == stack[-1]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)
        if not stack: return True
        return False

