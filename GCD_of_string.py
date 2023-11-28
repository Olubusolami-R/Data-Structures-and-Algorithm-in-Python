class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        test_str=""
        shorter=""
        if len(str1)>=len(str2):
            test_str=str2
        else:
            test_str=str1
        
        x=len(test_str)

        while x!=0:
            if len(str1)%len(test_str[:x])==0 and len(str2)%len(test_str[:x])==0:

                factor1=len(str1)//len(test_str[:x])
                factor2=len(str2)//len(test_str[:x])

                if ((str1[:x])*factor2)==str2 and ((str1[:x])*factor1)==str1:
                    return test_str[:x]
            x-=1
        
        #This solution has a great runtime but poor memory use (solution is generally memory intensive). Use a for loop with reverse range. 
        return ""
        