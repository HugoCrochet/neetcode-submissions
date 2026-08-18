class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
  
        s_list = [str(char) for char in s]
        t_list = [str(char) for char in t]
        return sorted(s_list) == sorted(t_list)

        