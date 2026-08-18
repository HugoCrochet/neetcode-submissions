class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "/"
        elif strs == [""]: return ""
        return '~'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "/" : return []
        elif s == "":return[""]        
        res = []
        j=0
        size_s = len(s)-1
        for i, char in enumerate(s):
            if char == '~':
                res.append(s[j:i])
                j = i+1
            elif i == size_s:
                res.append(s[j:i+1])
        return res

