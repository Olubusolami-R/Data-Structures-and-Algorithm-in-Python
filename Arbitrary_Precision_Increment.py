A=[0,3,6]
B=[9,9,9,9,9,9]

def addOne(arr):
    carry=0
    arr[len(arr)-1]+=1
    for i in reversed(range(0,len(arr))):   
        arr[i]+=carry
        carry=arr[i]//10
        
        if i==0:
            temp=arr[i]
            
        arr[i]=arr[i]%10
        
    if temp==10:
        arr[0]=1
        arr.append(0)
    return arr

print(addOne(A))
print(addOne(B))
