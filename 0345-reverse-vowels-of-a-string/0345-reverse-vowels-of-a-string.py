class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # string to list
        s_list = list(s)
        #set the left and right Index
        left, right = 0, len(s_list) - 1
        
        
        while left < right:
            #check left and right in vowels
            if s_list[left] in vowels and s_list[right] in vowels:
                #swap left and right
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s_list[left] in vowels:
                right -= 1
            else:
                left += 1
        
        return ''.join(s_list)