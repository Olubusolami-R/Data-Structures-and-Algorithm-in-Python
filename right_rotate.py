def right_rotate(lst, k):
    if len(lst)==0 or len(lst)==1 or len(lst)==k:
        return lst
    
    k= k % (len(lst))
    lst[:]=lst[-k:]+lst[:len(lst)-k]
    return lst