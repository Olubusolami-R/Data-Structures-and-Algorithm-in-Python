class Solution:
    def reverseWords(self, s: str) -> str:
        
        word=""
        reversed_str=""

        s=s.strip()

        for char in s:
            if char!=" ":
                word=word+char
            else:
                if word!="":
                    reversed_str=" "+word+reversed_str
                    word=""

        reversed_str=word+reversed_str   
        
        #or use this for better runtime
        s=s.split()
        s=s[::-1]
        return " ".join(s) 
        #or return reversed_str