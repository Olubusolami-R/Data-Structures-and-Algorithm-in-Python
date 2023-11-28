class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=len(word1)-1
        j=len(word2)-1
        maxlen=0
        text=""
        a=0

        if len(word1)>=len(word2):
            maxlen=len(word1)
        else:
            maxlen=len(word2)
        
        while a<maxlen:
            if a<=i:
                text=text + word1[a]

            if a<=j:
                text=text + word2[a]
            a+=1

        return text