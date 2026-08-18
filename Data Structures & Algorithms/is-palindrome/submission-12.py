class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1

        while lp < rp:
            # Move lp forward if it's not alphanumeric
            while lp < rp and not s[lp].isalnum():
                lp += 1
            # Move rp backward if it's not alphanumeric
            while lp < rp and not s[rp].isalnum():
                rp -= 1
            # Compare characters and return False if they don't match
            if s[lp].lower() != s[rp].lower():
                return False
            # Move pointers towards the center
            lp += 1
            rp -= 1

        return True