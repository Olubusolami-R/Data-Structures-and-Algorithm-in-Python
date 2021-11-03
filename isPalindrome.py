def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        temp=str(x)
        return temp==temp[::-1]
        """ 
        j=len(temp)-1
        i=0
        while i<len(temp) and j>0:
            if(temp[i]==temp[j]):
                i+=1
                j-=1
            else:
                return False
        return True"""

print(isPalindrome(24542))