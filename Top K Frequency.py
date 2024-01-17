class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        dictList = []
        arr = []
        for val in nums:
            if val in dict:
                dict[val]+=1
            else:
                dict[val] = 1
        print(dict)
        dictList = sorted(dict.items(), key = lambda x: x[1], reverse=True)
        print(dictList)
        for x in range(0,k):
            arr.append(dictList[x][0])
        return arr
