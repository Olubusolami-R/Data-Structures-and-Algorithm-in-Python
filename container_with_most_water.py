class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr=0
        rptr=len(height)-1
        max_area=0
        temp=0

        while lptr<rptr:

            temp=(rptr-lptr) * min(height[lptr],height[rptr])
            max_area=max(max_area,temp)

            if height[lptr]<height[rptr]:
                lptr+=1
            else:
                rptr-=1

        return max_area

        #note that a smaller ptr value means a smaller area. So when encountered on either sides, 
        #you try to get away fast. That's how you move the pointers.