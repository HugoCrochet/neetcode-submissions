class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for char in s.lower():
            if char.isalnum():
                new_s.append(char)
        return new_s == new_s[::-1]
        