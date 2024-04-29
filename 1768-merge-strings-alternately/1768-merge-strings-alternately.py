class Solution(object):
    def mergeAlternately(self, word1, word2):
        newword= ""
        list1= split(word1)
        list2= split(word2)
        diff, lenx, leny = 0, len(word1), len(word2)
        if lenx >= leny:  
            for i in range(leny):
                newword = newword + word1[i] + word2[i]
            newword= newword + word1[leny:]
        else:
            for i in range(lenx):
                newword = newword + word1[i] + word2[i]
            newword = newword + word2[lenx:]
        return newword
        