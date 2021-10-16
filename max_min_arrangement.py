def max_min(lst):
    a=0
    b=len(lst)-1
    mid=(len(lst))//2
    mylist=[]

    while a<b:
            mylist.append(lst[b])
            b-=1
            mylist.append(lst[a])
            a+=1

    if len(lst)%2 ==1:
        mylist.append(lst[mid])
        
    return mylist