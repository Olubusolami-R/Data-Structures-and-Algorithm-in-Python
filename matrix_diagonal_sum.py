class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        i=0
        j=len(mat)-1
        sum=0
        
        while(i<len(mat) and j>=0):
            if i==j:
                sum+=mat[i][i]
                i+=1
                j-=1
                continue
            else:
                sum+=mat[i][i]
                sum+=mat[i][j]
                i+=1
                j-=1
        return sum