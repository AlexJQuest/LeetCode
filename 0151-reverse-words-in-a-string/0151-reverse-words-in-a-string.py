class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.split()
        return ' '.join(slist[::-1])