class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi=max(candies)
        result=[]
        for i in candies:
            if i+extraCandies>=maxi:
                result.append(True)
            else:
                result.append(False)
        return result
                
        