class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        if len(nums) == 0:
            return 0
        sequenceLongest = 1
        currentSequence = [sortedList[0]]
        for x in range(1,len(sortedList)):
            if sortedList[x] - currentSequence [-1] == 1:
                currentSequence.append(sortedList[x])
            elif sortedList[x] - currentSequence [-1] > 1:
                currentSequence = [sortedList[x]]
            if len(currentSequence) > sequenceLongest:
                sequenceLongest = len(currentSequence)
        return sequenceLongest
