class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sar = sorted(list(s))
        tar = sorted(list(t))
        if sar==tar:
            return True
        return False
        
