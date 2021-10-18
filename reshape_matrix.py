def reshape(mat,r,c):
        if (r*c)!=(len(mat)*len(mat[0])):
            return mat
        if (r==len(mat)) and (c==len(mat[0])):
            return mat
        
        temp=[val for row in mat for val in row]
        
        lst=[[]]

        for i in range(r):
            lst.append([])
            for j in range(c):
                lst[i].append(temp[(c*i) + j])
        return lst[:-1]


#testcase
mat=[[1,2],[3,4],[5,6],[7,8]]
print(reshape(mat,2,4))