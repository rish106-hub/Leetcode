class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:  
            a = word.index(ch)  
            return word[:a+1][::-1] + word[a+1:]  
        return word  
