class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        grestestcandies = max(candies)
        result = [] 
        
        for i in range(len(candies)):
            result.append((candies[i] + extraCandies) >= grestestcandies)
        return result