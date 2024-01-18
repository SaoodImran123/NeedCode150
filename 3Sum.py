class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        targets = []
        solutions = set()
        for index in range(0,len(nums)):
            dict = {}
            target =  0 - nums[index]
            if target in targets:
                continue
            else:
                targets.append(target)
            for y in range(index+1,len(nums)):
                if nums[y] in dict and y != dict[nums[y]]:
                    tempSolution = tuple(sorted((nums[index],nums[dict[nums[y]]],nums[y])))
                    solutions.add(tempSolution)
                requisite = target-nums[y]
                dict[requisite] = y
        return list(solutions)
