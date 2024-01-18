class Solution:
    def maxArea(self, height: List[int]) -> int:
        dict = {}
        maxArea = 0
        startingPosition = 0
        endingPosition = len(height)-1
        while startingPosition != endingPosition:
            tempArea = self.getArea(height,startingPosition,endingPosition)
            if tempArea > maxArea:
                maxArea = tempArea
            if height[endingPosition] > height[startingPosition]:
                startingPosition += 1
            else:
                endingPosition -= 1
        return maxArea

    def getArea(self,height,index1,index2):
        maxHeight = min(height[index1], height[index2])
        area = maxHeight*(index2 - index1)
        return area
