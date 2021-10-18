def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        mylist=[[1],[1,1]]
        temp=[1]
        if numRows<=0:
            return []
        elif numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        elif numRows>2:
            for i in range(2,numRows):
                templist=[]
                templist.append(1)
                counter=0
                while counter+1<len(mylist[i-1]):
                    templist.append(mylist[i-1][counter]+mylist[i-1][counter+1])
                    counter+=1
                templist.append(1)
                mylist.append(templist)
        return mylist

print(generate(10))
                    
                
            