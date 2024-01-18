class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaS = ''.join(ch.lower() for ch in s if ch.isalnum())
        reverse = alphaS[::-1]
        if alphaS == reverse:
            return True
        return False
        
