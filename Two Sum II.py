class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for index in range(0,len(numbers)):
            if numbers[index] in dict and index != dict[numbers[index]]:
                return [dict[numbers[index]]+1,index+1]
            requisite = target-numbers[index]
            dict[requisite] = index
            # print(dict)
            # print("index:" , index)




        
