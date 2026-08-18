class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_dict, t_dict = {}, {}
        for letter in zip(s,t):
            s_dict[letter[0]] = s_dict.get(letter[0],0)+1
            t_dict[letter[1]] = t_dict.get(letter[1],0)+1
        for a in s_dict.items():
            if t_dict.get(a[0],0) != a[1]: return False
        return True

