class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels= ['a', 'e','i','o','u','A','E','I','O','U']
        #Observe the runtime difference between using a string and a list woah
        vowels="aeiouAEIOU"
        i=0
        j=len(s)-1
        output=[""]*len(s)

        while i<=j:
            if s[i] not in vowels:
                output[i]=s[i]
                i+=1
            else:
                if s[j] not in vowels:
                    output[j]=s[j]
                    j-=1
                else:
                    output[i] = s[j]
                    output[j]=s[i]
                    i+=1
                    j-=1

        return ''.join(output)





                


        