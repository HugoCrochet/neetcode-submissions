class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
        }
        st = deque()

        for char in s: 
            if char in mapping: 
                if len(st) > 0: 
                    if st[-1] == mapping[char]: st.pop()
                    else: return False
                else: return False
            else: st.append(char)

        if len(st) > 0: return False
        return True 