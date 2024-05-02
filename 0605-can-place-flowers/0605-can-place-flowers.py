class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            #check flowerbed
            if flowerbed[i] == 0:
                #check left: 
                potleft = (i == 0) or (flowerbed[i-1] ==0)
                #check right: 
                potright = ( i == len(flowerbed) -1) or (flowerbed[i+1] ==0)
                # if left and right empty , plant
                if potleft & potright:
                    planted +=1
                    flowerbed[i] = 1
                    if planted >= n:
                        return True
        return planted >= n
            