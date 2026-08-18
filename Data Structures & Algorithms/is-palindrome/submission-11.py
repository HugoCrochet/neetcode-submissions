class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        for i in range(len(s)//2):
            while (not s[lp].isalnum()) and lp<len(s)-1:
                lp += 1 
            while (not s[rp].isalnum()) and rp>0:
                rp -= 1                 
            if s[rp].isalnum() and s[lp].isalnum() and not s[lp].lower() == s[rp].lower(): 
                return False
            if lp<len(s): lp += 1
            if rp>0: rp -= 1
        return True

