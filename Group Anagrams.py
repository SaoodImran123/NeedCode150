class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in dict:
                dict[sortedWord].append(word)
            else:
                dict[sortedWord] = [word]
        return dict.values()
        
