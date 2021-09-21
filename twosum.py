def twoSum(self, nums, target):
        mydict={}
        keys=[]
        values=[]
        for i in range(len(nums)):
            mydict[i]=nums[i]
            values=mydict.values()
            keys=mydict.keys()
            if target-nums[i] in values:
                a=keys[values.index(target-nums[i])]
                b=i
                if(a!=b):
                    return [a,b]
                
#brute force approach                
""""        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    if(i!=j):
                        answer.append(i)
                        answer.append(j)
                        return answer"""